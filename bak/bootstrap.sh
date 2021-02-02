#!/bin/bash
set -e
: <<'PlutoChan'
Author: Pluto Chan
Usage: This is a common init script for spring boot projects
command line example:
./bootstrap.sh project service action
PlutoChan
args=3
#error code settings
E_MUSTNONEROOT=55
E_ARGSERROR=56
E_TOOMANYJAR=57
E_FILENOTFOUND=58
E_ALREADYSTARTED=59
E_TOOMANYPROC=60
#import enviroment variables
source /etc/profile && source $HOME/.bashrc && source $HOME/.profile
#check for a series of conditions
[[ $EUID -eq 0 ]] && echo "must not run as root" && exit ${E_MUSTNONEROOT}
#get absolute path of the script
base_dir=$(cd $(dirname $0) && pwd)
#must be 2 or 3 args
[[ $# -ne "$args" -o $# -ne "$(($args-1))" ]] && echo "must be $args or $(($args-1)) args" && exit ${E_ARGSERROR}
if [ $# -eq "$args" ] 
then 
    project=$1 && service=$2 && action=$3
    [[ ! -d "${base_dir}/$project/$service" ]] && echo "project or serivce not found" && exit ${E_ARGSERROR}
    svc_dir="${base_dir}/$project/$service"
else
    service=$1 && action=$2
    svc_dir="${base_dir}/$service"
fi
#echo "service direcotry:   ${base_dir}/$project/$service"
#config settings
app_name=$(basename $(ls -1 ${svc_dir}/*.jar))
app_jar=${svc_dir}/$app_name
conf=${svc_dir}/application.properties
log=${svc_dir}/logback.xml
port_file=${svc_dir}/../port-usage.txt
port=$(grep "$service" ${port_file} |cut -d: -f2)
WAIT=5
XMS=1024m
XMX=2048m
java=$(which java)
[[ "$(ls -1 ${base_dir}/$project/$service/*.jar|wc -l)" -gt 1 ]] && echo "too many jar file in the service directory!" && exit ${E_TOOMANYJAR}
[[ -z "$java" ]] && echo "java not found" && exit ${E_FILENOTFOUND}
[ ! -f "$conf"  -o ! -f "$log" ] && echo "main config file or log config file not found" && exit ${E_FILENOTFOUND}
[[ ! -d "${svc_dir}/logs" ]] && mkdir "${svc_dir}/logs"
JAVA_OPTS="-server -Xms$XMS -Xmx$XMX -Xloggc:${svc_dir}/logs/gc.log -verbose:gc -XX:+PrintGCDetails -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=${svc_dir}/logs" 
APP_OPTS="--spring.profiles.active=product --spring.config.location=$conf --logging.config=$log --spring.server.port=$port"
for i in ${svc_dir}/lib/*
do 
    CLASS_PATH=$i:"$CLASS_PATH"
done

#check process, kill redundant
check_ps(){
    pid=$(ps -ef|grep ${app_jar}|grep -v 'grep'| awk '{print $2}')
    [[ -n "$pid" ]] && proc_cnt=$(echo $pid |tr ' ' '\n' |wc -l) || proc_cnt=0
    if [ "${proc_cnt}" -gt 1 ]
    then 
        echo $pid|tr ' ' '\n'|xargs kill -HUP
    fi
}

check_ps
echo "pid: $pid"
echo "process count: ${proc_cnt}"
#start JVM
java_start(){
    #$java $JAVA_OPTS -jar ${app_jar} $APP_OPTS >/dev/null 2>&1 &
    echo "$java $JAVA_OPTS -jar ${app_jar} $APP_OPTS"
    $java $JAVA_OPTS -jar ${app_jar} $APP_OPTS
    echo "start successfully, pid is $!"
}
#show waiting status
waiting(){ 
    local seconds=$1 
    for i in `seq 1 $seconds`
    do 
        sleep 1 
        ((exptime++)) 
        echo -n -e "\rWaitting: $exptime..." 
    done 
    echo -n -e "\n" 
}

app_start(){
    echo "starting $project $service"
    if [ "${proc_cnt}" -eq 1 ] 
    then
        pid=$(ps -ef|grep ${app_jar}|grep -v grep|awk '{print $2}')
        echo "process already started, pid is $pid" && exit ${E_ALREADYSTARTED}
    elif [ "${proc_cnt}" -gt 1 ] 
    then
        echo "too many process, please restart service" && exit ${E_TOOMANYPROC}
    else 
        java_start
    fi
}

#start service as foreground mode
app_console(){
    echo -n "starting $project $service foreground"
    if [ "${proc_cnt}" -eq 1 ]
    then
        pid=$(ps -ef|grep ${app_jar}|grep -v grep|awk '{print $2}')
        echo "already running as pid $pid" && exit ${E_ALREADYSTARTED}
    elif [ "${proc_cnt}" -gt 1 ]
    then
        ps -ef|grep ${app_jar}|grep -v grep| awk '{print $2}'|xargs kill -HUP > /dev/null 2>&1
        #may be need kill forcible
        #ps -ef|grep ${app_jar}|grep -v grep| awk '{print $2}'|xargs kill -SIGKILL > /dev/null 2>&1
        #java_start
        #$java $JAVA_OPTS -classpath .:$CLASS_PATH $CLASS $APP_OPTS
        $java $JAVA_OPTS -jar ${app_jar} $APP_OPTS

    else
        java_start
    fi
}

app_stop(){
    if [ "${proc_cnt}" -eq 0 ];then
      echo "$APP_NAME is not running." && exit
    fi
    echo "$HOSTNAME: stopping $service $pid ... "
    kill -HUP $pid > /dev/null 2>&1

    if [ "$?" -eq 0 ]
    then
        echo "stopped success"
    else 
        kill -SIGKILL $pid > /dev/null 2>&1
    fi
}

app_restart(){
    if [ ${proc_cnt} -ge 1 ]
    then
      app_stop
      waiting $WAIT
    fi
    check_ps
    app_start
}

app_status(){
    if [ ${proc_cnt} -eq 1 ]
    then
        pid=$(ps -ef|grep ${app_jar}|grep -v grep|awk '{print $2}')
        echo "$service $pid is running"
    else
        #may be failed to kill
        ps -ef | grep ${app_jar} | grep -v grep | awk -F '{print $2}'|xargs kill -HUP > /dev/null 2>&1
        echo "$service  is Stop"
    fi
}

case "$3" in 
    start) app_start;; 
    console) app_console;; 
    stop) app_stop;; 
    restart) app_restart;; 
    status) app_status;; 
    *) echo "Usage: $0 project service {console|start|stop|restart|status}" && exit ${E_ARGSERROR} ;; 
esac


: <<'commented'
#APP_NAME=gjyf-jobcenter-admin-2.0.2
#BASE=$(dirname $bin_path)
#echo $BASE
#echo $bin_path
#echo $conf
#echo $log
#CLASS='com.xxl.job.admin.XxlJobAdminApplication'
#app_jar=${svc_dir}/lib/${APP_NAME}.jar

export LANG=en_US.UTF-8
export BASE=$BASE
#echo $conf
#echo $conf
if [ -z "$java" ] ; then
fi

if [ -z "$java" ]; then
     echo "Cannot find a java JDK. Please set either set java or put java (>=1.8) in your PATH." 2>&2
     exit 1
fi

if [[ $# -eq 2 ]]; then
    profile=$2
fi
#echo $conf
#1.输出进程|过滤除class以外的进程|输出第二字段（pid）
#2.打印pid|去除空格转行|统计输出个数
#3.大于2 杀死进程
# Source function library.
#. /etc/init.d/functions
    #tail -f ${CATALINA_OUT}

        #echo '-------------------------------------'
        #echo $JAVA_OPTS
        #echo $APP_OPTS
        #echo $java
        #echo $CLASS_PATH
        #echo $CLASS
        #echo '-------------------------------------'
        
        #echo  ${java} ${JAVA_OPTS} -classpath .:$CLASS_PATH $CLASS $APP_OPTS 
        #echo  ${java} ${JAVA_OPTS} -jar ${app_jar} $APP_OPTS 

        #${java} ${JAVA_OPTS} -classpath .:$CLASS_PATH $CLASS $APP_OPTS 1>/dev/null 2>&1 &
commented
