# -*- coding: utf8 -*-
import jieba,os,pyodbc
import pandas as pd
from pandas import DataFrame,Series

def wordcut_fun(wordcut,excelsum,exceldetail):
    result=[]
    #��ԭʼ���ݵ���������γ�list
    wordcuts=wordcut.split("\n")
    #���зִʲ���
    for i in wordcuts:
        try:
            seg_list = jieba.cut(i) 
            for j in seg_list:
                if len(j)>=2:
                    result.append(j.lower())
        except: print("some wrong")

    dic_result={}
    #���м���
    for i in result:
        if i in dic_result:
            dd=dic_result.get(i)
            dic_result[i]=dd+1
        else:
            dic_result[i]=1
    dic_result=sorted(dic_result.items(),key=lambda asd:asd[1],reverse=True)
    dic_data=DataFrame(dic_result,columns=['keyword','frequency'])
    dic_data['tag']=''
    #�������������Լ����Ķ��������ǩ
    source=pd.read_sql_query(r'select fenci as keyword,tag_keyword as tag from [zln_data].[dbo].[lagou_fenci_jd]',con=sqlconn)
    for i in list(range(len(dic_data['keyword']))):
        for t in list(range(len(source['keyword']))):
            if source.ix[t,'keyword'].lower() in dic_data.ix[i,'keyword']:
                dic_data.ix[i,'tag']=source.ix[t,'tag']
    dic_data=dic_data[dic_data['tag']!='']
    sum_data=dic_data['frequency'].groupby(dic_data['tag']).sum()
    
    #д��excel��
    DataFrame(dic_data).to_excel(exceldetail+'.xls',sheet_name='detail')
    DataFrame(sum_data).to_excel(excelsum+'.xls',sheet_name='sum')

if __name__== '__main__':
    sql=input('������sql��ѯ��䣨����֮����س�����')
    excel1=input('������--��ϸ�б�--���ļ���(������׺��)��')
    excel2=input('������--�����б�--���ļ�����������׺������')
    #***����Ϊ���ݿ�ĵ�ַ���˺ź�����
    sqlconn=pyodbc.connect("DRIVER={SQL SERVER};SERVER=***\\sql;DATABASE=zln_data;UID=***;PWD=***")#�����ݿ�����ȡ�����Сֵ
    sqlcursor=sqlconn.cursor()
    jd=pd.read_sql_query(sql,con=sqlconn)
    t=wordcut_fun(wordcut=r'\n'.join(jd['jd']),exceldetail=excel1,excelsum=excel2)