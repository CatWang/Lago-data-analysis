# -*- coding:utf-8 -*-
import requests,json,re,time,datetime,socket,pyodbc
from urllib import request
import pandas as pd
from pandas import DataFrame,Series
from bs4 import BeautifulSoup

def lagou_spider_keyword(keyword):
    #�������ַ���ת��Ϊutf-8���룬֮�����lagou.com����url����
    keywordbyte=keyword.encode('utf-8')
    keywordindex=str(keywordbyte).replace(r'\x','%').replace(r"'","")
    keywordindex=re.sub('^b','',keywordindex)

    #�����ܹ��ж����������ҳ
    i =0
    type='true'
    url='http://www.lagou.com/jobs/positionAjax.json?px=default&first='+type+'&kd='+keywordindex+'&pn='+str(i+1)
    with request.urlopen(url) as f:
        data=f.read()
        urlcount=int(json.loads(str(data,encoding='utf-8',errors='ignore'))["content"]["totalPageCount"])
        print('��������ҳ�湲��%d'%urlcount)

    #��ʼ��ʽץȡ
    for i in list(range(0,urlcount)):

        #����ҳ��
        if i ==0 :
            type='true'
        else:
            type='false'
        url='http://www.lagou.com/jobs/positionAjax.json?px=default&first='+type+'&kd='+keywordindex+'&pn='+str(i+1)
        with request.urlopen(url) as f:
            data=f.read()

        #��ȡjson���ݣ���ʼ����
        try:
            jsondata=json.loads(str(data,encoding='utf-8',errors='ignore'))["content"]['result']

            for t in list(range(len(jsondata))):
                #��company�������б�ϲ�Ϊһ���ַ���
                jsondata[t]['companyLabelList2']='-'.join(jsondata[t]['companyLabelList'])
                jsondata[t].pop('companyLabelList')

                #��ÿһ����������Series��֮���ٺϲ�
                if t == 0:
                    rdata=DataFrame(Series(data=jsondata[t])).T
                else:
                    rdata=pd.concat([rdata,DataFrame(Series(data=jsondata[t])).T])
            #���¸�rdata����
            rdata.index=range(1,len(rdata)+1)
            rdata['keyword']=keyword
            rdata['salarymin']=0
            rdata['salarymax']=0
            rdata['url']=''
            rdata['jd']=''#ְλ����
            rdata['handle_perc']=''#������ʱ�����ʣ��������ڴ��������ռ���м����ı���
            rdata['handle_day']=''#��ɼ�������ƽ������
            for klen in list(range(len(rdata['salary']))):
                rdata.ix[klen+1,'salarymin'] = re.search('^(\d*?)k',rdata['salary'].iloc[klen]).group(1)
                #������ʵ����ֵû��д���磨8k���ϣ�������Ϊ��ֵ
                if re.search('-(\d*?)k$',rdata['salary'].iloc[klen]) != None:
                    rdata.ix[klen+1,'salarymax'] = re.search('-(\d*?)k$',rdata['salary'].iloc[klen]).group(1)
                else:
                    rdata.ix[klen+1,'salarymax'] = ''
                #����urlһ�У����ں���ץȡjd����
                rdata.ix[klen+1,'url'] =  'http://www.lagou.com/jobs/%s.html'% rdata.ix[klen+1,'positionId']

                #��url���ж���ץȡ����jdץ����
                with request.urlopen(rdata.ix[klen+1,'url']) as f:
                    data_url=f.read()
                    soup_url=BeautifulSoup(data_url,'html5lib')
                    strings_url=soup_url.find('dd',class_='job_bt').strings
                    rdata.ix[klen+1,'jd']=''.join(strings_url).encode('gbk','ignore').decode('gbk','ignore').replace(' ','')
                    temp=soup_url.find_all('span',class_='data')
                    if re.search('>(\w*%)<',str(temp[0])) == None:
           