#coding:utf-8
import urllib2
import urllib
import csv
import json
import codecs
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
    'Host': 'www.lagou.com',
    'Origin': 'http://www.lagou.com',
    'Referer': 'http://www.lagou.com/zhaopin/Java/?labelWords=label',
    'Cookie': 'LGMOID=20151221133025-13872EFC4C9A30161B385C5123184A1F; user_trace_token=20151221133026-f0b87a3c-a7a3-11e5-86e4-525400f775ce; LGUID=20151221133026-f0b8818a-a7a3-11e5-86e4-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; hideOnekeyBanner=1; JSESSIONID=C6707C1BC0977C1154A142BF351E2F1D; HISTORY_POSITION=93055%2C30k-60k%2C%E8%98%91%E8%8F%87%E8%A1%97%2CC%2B%2B%7C; PRE_UTM=; PRE_HOST=; PRE_SITE=http%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=http%3A%2F%2Fwww.lagou.com%2Fzhaopin%2Fquanzhangongchengshi%2F%3FlabelWords%3Dlabel; _gat=1; SEARCH_ID=2e388e0da5614ddf9faad71d4bbf921d; _ga=GA1.2.679801410.1450675826; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1450675826,1450692327; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1450699349; LGSID=20151221194859-d2e3db72-a7d8-11e5-872e-525400f775ce; LGRID=20151221200229-b592397a-a7da-11e5-872e-525400f775ce',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding' :'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection' : 'keep-alive'
}
DOWNLOAD_URL = 'http://www.lagou.com/jobs/positionAjax.json?'



if __name__ == '__main__':
    with open('csvs/jishu/ASP.csv', 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8)

        csvfile.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n' % (u'职位'.encode('utf-8'), u'工资'.encode('utf-8'), u'经验要求'.encode('utf-8') , u'职位一级分类'.encode('utf-8'), u'职位二级分类'.encode('utf-8'), u'公司名称'.encode('utf-8'), u'城市'.encode('utf-8'), u'学历'.encode('utf-8'), u'公司规模'.encode('utf-8'), u'公司阶段'.encode('utf-8'), u'公司业务领域'.encode('utf-8')))

        hasNextPage = True
        i = 0
        while (hasNextPage):
            i += 1
            values = {
                'first': 'false',
                'pn': str(i),
                'kd': 'ASP'
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(DOWNLOAD_URL, data = data, headers=headers)
            resp = urllib2.urlopen(req)
            html = resp.read().decode('utf-8')
            positions = json.loads(html)
            hasNextPage = positions['content']['hasNextPage']
            j = 0
            while (j < 15):
                companyName = positions['content']['result'][j]['companyName']
                positionId = positions['content']['result'][j]['positionId']
                city = positions['content']['result'][j]['city']
                companyId = positions['content']['result'][j]['companyId']
                education = positions['content']['result'][j]['education']
                companySize = positions['content']['result'][j]['companySize']
                financeStage = positions['content']['result'][j]['financeStage']
                financeStage = financeStage[0:financeStage.find('(')]
                print(financeStage)
                industryField = positions['content']['result'][j]['industryField']
                positionName = positions['content']['result'][j]['positionName']
                positionFirstType = positions['content']['result'][j]['positionFirstType']
                positionSecondType = positions['content']['result'][j]['positionType']
                format = '0123456789'
                if not '-' in companySize:
                    format = '0123456789'
                    for c in companySize:
                        if not c in format:
                            companySize = companySize.replace(c, '')
                else:
                    companySize = companySize[0:companySize.find('-')]
                print(companySize)
                salary = positions['content']['result'][j]['salary']
                if not '-' in salary:
                    salary = salary[0: salary.find('k')]
                else:
                    salary = (int(salary[0:salary.find('k')]) + int(salary[salary.find('-')+1:len(salary)-1])) / 2
                workYear = positions['content']['result'][j]['workYear']
                workYear = workYear[0:workYear.find('-')]
                csvfile.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n' % ((positionName).encode('utf-8'), str(salary), workYear.encode('utf-8'), positionFirstType.encode('utf-8'), positionSecondType.encode('utf-8'), companyName.encode('utf-8'), city.encode('utf-8'), education.encode('utf-8'),companySize.encode('utf-8'),financeStage.encode('utf-8'), industryField.encode('utf-8')))
                j += 1