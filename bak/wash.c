#include<stdio.h>
#include<stdlib.h>
#include<time.h>
/* 
此程序就做为struct tm的学习范例，封存起来
*/
void main(int argc, char *argv[]) 
{
    //先拿年月，并判定是否为刷洗月
    int year=atoi(argv[1]);
    int month=atoi(argv[2]);
    if (month<1 || month>12) {
        printf("month %d illegal!\n",month);
        exit(1);
    } else if (month % 2 ==0) {
        printf("%d is not odd month\n",month);
        exit(1);
    }
    //创建日期时间结构与相应时间戳
    struct tm p;
    p.tm_year=year-1900;
    //实际月份为1～12,但在结构上，表示为0～11,因此要-1再赋值
    p.tm_mon=month-1;
    p.tm_mday=1;
    p.tm_hour=0;
    p.tm_min=0;
    p.tm_sec=0;
    p.tm_isdst=0;
    //printf("init month: %d\n",p.tm_mon);
    //利用下月的第一天，减一小时，得到前一天的时间戳，反过来利用该时间戳，得到当月的天数
    if (p.tm_mon==11) {
        p.tm_mon=0;
        p.tm_year+=1;
    } else 
        p.tm_mon+=1;
    time_t tmp_time=mktime(&p);
    printf("%ld\n",tmp_time);
    time_t last_day=tmp_time - 60*60;
    printf("%ld\n",last_day);
    struct tm *q=localtime(&last_day);
    int total_days=q->tm_mday;
    printf("%d\n",total_days);
    char *s;
    s = (char *)malloc(sizeof(char)*20);
    strftime(s,20,"%Y-%m-%d %H:%M:%S",q);
    printf("%s\n",s);
}