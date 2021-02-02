#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int get_int(FILE *fp) 
{
    int *i;
    i = (int *)malloc(sizeof(int)); 
    fread(i,4,1,fp);
    return *i;
}
float get_float(FILE *fp) 
{
    float *f;
    f = (float *)malloc(sizeof(float)); 
    fread(f,4,1,fp);
    return *f;
}
char  *get_str(FILE *fp,int len) 
{
    char *s;
    s = (char *)malloc(sizeof(char)*len); 
    fread(s,len,1,fp);
    return s;
}
void main() 
{
    FILE *fp;   
    const char *fn="m08-4.mst";
    fp = fopen(fn,"rb");    
    //先取记录数
    int recs=get_int(fp);
    printf("records: %d\n",recs);
    for (int j=1;j<=recs;j++) {
        printf("record %d begins\n",j);
        #define MAX_LEN 500
        char *field,*mst_id,*model,*init_coor,*coor2,*coor3,*mst_list,*fix2,*info;
        field = (char *)malloc(sizeof(char)*MAX_LEN); 
        //编号
        mst_id = (char *)malloc(sizeof(char)*MAX_LEN); 
        sprintf(mst_id,"%s",get_str(fp,get_int(fp)));
        //模型
        model = (char *)malloc(sizeof(char)*MAX_LEN); 
        sprintf(model,"%s",get_str(fp,get_int(fp)));
        //初始坐标及坐标2
        init_coor = (char *)malloc(sizeof(char)*MAX_LEN); 
        sprintf(init_coor,"%5.3f, %5.3f ,%5.3f",get_float(fp),get_float(fp),get_float(fp));
        coor2 = (char *)malloc(sizeof(char)*MAX_LEN); 
        sprintf(coor2,"%5.3f, %5.3f ,%5.3f",get_float(fp),get_float(fp),get_float(fp));
        //固定的1
        int fix1=get_int(fp);
        //坐标3
        coor3 = (char *)malloc(sizeof(char)*MAX_LEN); 
        sprintf(coor3,"%5.3f, %5.3f ,%5.3f",get_float(fp),get_float(fp),get_float(fp));
        //怪物数量
        int mst_no=get_int(fp);
        //具体怪物ID
        mst_list = (char *)malloc(sizeof(char)*MAX_LEN); 
        for(int i=1; i<=mst_no;i++) {
            char *tmps;
            tmps = (char *)malloc(sizeof(char)*MAX_LEN); 
            sprintf(tmps,"%d, ",get_int(fp));
            strcat(mst_list,tmps);
        }
        mst_list[strlen(mst_list)-2]=0;
        //两个固定的1
        fix2 = (char *)malloc(sizeof(char)*MAX_LEN); 
        sprintf(fix2,"%d, %d",get_int(fp),get_int(fp));
        //开始了行为部分，先读字段名
        char *pos,*s1;
        int i1,i2,i3,i4;
        float f1;
        info = (char *)malloc(sizeof(char)*MAX_LEN*2); 
        s1 = (char *)malloc(sizeof(char)*MAX_LEN); 
        sprintf(field,"%s",get_str(fp,get_int(fp)));
        //读第一个参数，基本全是0
        i1=get_int(fp);
        //第二个参数很关键，如果是1,那么为复杂记录，0则为简单对象
        int beh_parm2=get_int(fp);
        if (beh_parm2==1) {
            sprintf(field,"%s: %d, %d;\n",field,i1,beh_parm2);
            strcat(info,field);
            do {
                sprintf(field,"%s",get_str(fp,get_int(fp)));
                //第一个参数为字符串的字段
                if (((pos=strstr(field,"GroupName"))!=NULL) || ((pos=strstr(field,"GroupPathWayID"))!=NULL))  {
                    sprintf(s1,"%s",get_str(fp,get_int(fp)));
                    i2=get_int(fp);
                    sprintf(field,"%s: %s, %d;\n",field,s1,i2);
                    strcat(info,field);
                } else if (((pos=strstr(field,"ObjectExpectTime"))!=NULL) || 
                ((pos=strstr(field,"ObjectWaitTime"))!=NULL) ||
                ((pos=strstr(field,"run_max_force"))!=NULL) ||
                ((pos=strstr(field,"run_max_speed"))!=NULL)) {
                    f1=get_float(fp);
                    i2=get_int(fp);
                    sprintf(field,"%s: %5.3f, %d;\n",field,f1,i2);
                    strcat(info,field);
                } else if ((pos=strstr(field,"walk_pathfollow"))!=NULL) {
                    i1=get_int(fp);
                    i2=get_int(fp);
                    i3=get_int(fp);
                    i4=get_int(fp);
                    sprintf(field,"%s: %d, %d, %d, %d;\n",field,i1,i2,i3,i4);
                    strcat(info,field);
                } else {
                    i1=get_int(fp);
                    i2=get_int(fp);
                    sprintf(field,"%s: %d, %d;\n",field,i1,i2);
                    strcat(info,field);
                }
            } while ((pos=strstr(field,"walk_pathfollow"))==NULL);
        } else if (beh_parm2==0) {
            i3=get_int(fp);
            i4=get_int(fp);  
            sprintf(field,"%s: %d, %d, %d, %d;\n",field,i1,beh_parm2,i3,i4);
            strcat(info,field);     
        }
        do {
            sprintf(field,"%s",get_str(fp,get_int(fp)));
            //第一个参数为字符串的字段
            if ((pos=strstr(field,"max_pursuit_speed"))!=NULL) {
                f1=get_float(fp);
                i2=get_int(fp);
                sprintf(field,"%s: %5.3f, %d;\n",field,f1,i2);
                strcat(info,field);
            } else {
                i1=get_int(fp);
                i2=get_int(fp);
                sprintf(field,"%s: %d, %d;\n",field,i1,i2);
                strcat(info,field);
            }
        } while ((pos=strstr(field,"max_pursuit_speed"))==NULL);
        //接下来很关键，要判断接下来是脚本函数，还是到了下一条记录的编号部分，因此，先要记录位置
        long loc=ftell(fp);
        sprintf(field,"%s",get_str(fp,get_int(fp)));
        if ((pos=strstr(field,"script_func"))!=NULL) {
            i1=get_int(fp);
            i2=get_int(fp);
            if (i2!=0) {
                sprintf(s1,"%s",get_str(fp,get_int(fp)));
                i3=get_int(fp);
                i4=get_int(fp);
                sprintf(field,"%s: %d, %d, %s, %d, %d;\n",field,i1,i2,s1,i3,i4);
            } else {
                sprintf(field,"%s: %d, %d;\n",field,i1,i2);
            }
            strcat(info,field);
        } else {
            fseek(fp,loc,SEEK_SET);
        }
        printf("%s\n",info);
        printf("record %i ends\n\n\n",j);
    }
    fclose(fp);
}
