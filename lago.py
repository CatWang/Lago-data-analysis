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
    'Cookie': 'JSESSIONID=C6707C1BC0977C1154A142BF351E2F1D; LGMOID=20151221133025-13872EFC4C9A30161B385C5123184A1F; user_trace_token=20151221133026-f0b87a3c-a7a3-11e5-86e4-525400f775ce; LGUID=20151221133026-f0b8818a-a7a3-11e5-86e4-525400f775ce; PRE_UTM=AD__baidu_pinzhuan; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D0fKL00c00fA-iwf0g0Fw0FNkUsKsWMIy000007KSy1s00000AkDWg9.THL0oUhY0A3qmh7GuZR0T1dbrADdPW9-rH0snjRzrj0v0ZRqrDDdrj6LrHnsfW-7f177rjfYrjNAfYm3wbuKnHcYwRc0mHdL5iuVmv-b5Hc1P1f1PHnsPWThTZFEuA-b5HDvFhqzpHYkFMPdmhqzpHYhTZFG5Hc0uHdCIZwsrBtEILILQhk9uvqdQhPEUitOIgwVgLPEIgFWuHdKw7qxmh7GuZNxTA-8Xh9dmy3hIgwVgvd-uA-dUHd1uyYhIgwVgvP9UgK9pyI85NP7HfKWThnqnHb1PH0%26tpl%3Dtpl_10085_12986_1%26l%3D1012629072%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE; PRE_LAND=http%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3DAD__baidu_pinzhuan%26utm_medium%3Dsem%26utm_campaign%3DSEM; index_location_city=%E5%85%A8%E5%9B%BD; hideOnekeyBanner=1; _gat=1; SEARCH_ID=fd687a5bf42a4a23bc41ad88ff2a62b9; _ga=GA1.2.679801410.1450675826; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1450675826,1450692327; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1450693333; LGSID=20151221180527-5be646d1-a7ca-11e5-872e-525400f775ce; LGRID=20151221182212-b35c70cf-a7cc-11e5-89c4-5254005c3644',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding' :'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection' : 'keep-alive',
}
DOWNLOAD_URL = 'http://www.lagou.com/jobs/positionAjax.json?'
words1 = ['游戏策划', '产品实习生', '网页产品设计师', '无线产品设计师', '产品部经理', '产品总监']
words = ['Java', 'Python', 'PHP', '.NET', 'C#', 'C++', 'C', 'VB', 'Delphi', 'Perl', 'Hadoop', 'Node.js', '数据挖掘', '自然语言处理', '搜索算法', '精准推荐', '全栈工程师', 'Go', 'ASP', 'Shell', 'HTML5', 'Android', 'iOS', 'WP', 'web前端', 'Flash', 'html5', 'JavaScript', 'U3D', 'COCOS2D-X', '测试工程师', '自动化测试', '功能测试', '性能测试', '测试开发', '游戏测试', '白盒测试', '灰盒测试', '黑盒测试', '手机测试', '硬件测试', '测试经理', '运维工程师', '运维开发工程师', '网络工程师', '系统工程师', 'IT支持', 'IDC', 'CDN', 'F5', '系统管理员', '病毒分析', 'WEB安全', '网络安全', '系统安全', '运维经理', 'MySQL', 'SQLServer', 'Oracle', 'DB2', 'MongoDB', 'ETL', 'Hive', '数据仓库', '技术经理', '技术总监', '架构师', 'CTO', '运维总监', '技术合伙人', '项目总监', '测试总监', '安全专家', '项目经理', '项目助理', '硬件', '嵌入式', '自动化', '单片机', '电路设计', '驱动开发', '系统集成', 'FPGA开发', 'DSP开发', 'ARM开发', 'PCB工艺', '模具设计', '热传导', '材料工程师', '精益工程师', '射频工程师', '实施工程师', '售前工程师', '售后工程师', 'BI工程师', '产品经理', '网页产品经理', '移动产品经理', '产品助理', '数据产品经理', '电商产品经理', '游戏策划', '产品实习生', '网页产品设计师', '无线产品设计师', '产品部经理', '产品总监', '游戏制作人', '网页设计师', 'Flash设计师', 'APP设计师', 'UI设计师', '平面设计师', '美术设计师（2D+3D）', '广告设计师', '多媒体设计师', '原画师', '游戏特效', '游戏界面设计师', '视觉设计师', '游戏场景', '游戏角色', '游戏动作', '数据分析师', '用户研究员', '游戏数值策划', '设计经理/主管', '设计总监', '视觉设计经理/主管', '视觉设计总监', '交互设计经理/主管', '交互设计总监', '用户研究经理/主管', '用户研究总监', '网页交互设计师', '交互设计师', '无线交互设计师', '硬件交互设计师', '内容运营', '产品运营', '数据运营', '用户运营', '活动运营', '商家运营', '品类运营', '游戏运营', '网络推广', '运营专员', '网店运营', '新媒体运营', '海外运营', '运营经理', '副主编', '内容编辑', '文案策划', '记者', '售前咨询', '售后咨询', '淘宝客服', '客服经理', '主编', '运营总监', 'COO', '客服总监', '市场策划', '市场顾问', '市场营销', '市场推广', 'SEO', 'SEM', '商务渠道', '商业数据分析', '活动策划', '网络营销', '海外市场', '政府关系', '媒介经理', '广告协商', '品牌公关', '销售专员', '销售经理', '客户代表', '大客户代表', 'BD经理', '渠道销售', '代理商销售', '销售助理', '电话销售', '销售顾问', '商品经理', '市场总监', '销售总监', '商务总监', 'CMO', '公关总监', '采购总监', '投资总监', '物流', '仓储', '采购专员', '采购经理', '商品经理', '分析师', '投资顾问', '投资经理', '人事/HR', '培训经理', '薪资福利经理', '绩效考核经理', '人力资源', '招聘', 'HRBP', '员工关系', '助理', '前台', '行政', '总助', '文秘', '会计', '出纳', '财务', '结算', '税务', '审计', '风控', '行政总监/经理', '财务总监/经理', 'HRD/HRM', 'CFO', 'CEO', '法务', '法律', '专利', '投资助理', '融资', '并购', '行业研究', '投资者关系', '资产管理', '理财顾问', '交易员', '资信评估', '合规稽查', '律师', '清算', '融资总监', '并购总监', '风控总监', '副总裁']


if __name__ == '__main__':
    with open('csvs/yunying/yunying/wangluoTuiguang.csv', 'wb') as csvfile:
        csvfile.write(codecs.BOM_UTF8)

        csvfile.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n' % (u'职位'.encode('utf-8'), u'工资'.encode('utf-8'), u'经验要求'.encode('utf-8') , u'职位一级分类'.encode('utf-8'), u'职位二级分类'.encode('utf-8'), u'公司名称'.encode('utf-8'), u'城市'.encode('utf-8'), u'学历'.encode('utf-8'), u'公司规模'.encode('utf-8'), u'公司阶段'.encode('utf-8'), u'公司业务领域'.encode('utf-8')))
        print('write a row!')
        hasNextPage = True
        i = 0
        while (hasNextPage):
            i += 1
            values = {
                'first': 'false',
                'pn': str(i),
                'kd': '网络推广'
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(DOWNLOAD_URL, data = data, headers=headers)
            resp = urllib2.urlopen(req, timeout=30)
            html = resp.read().decode('utf-8')
            positions = json.loads(html)
            hasNextPage = positions['content']['hasNextPage']
            itemNum = 15
            if (hasNextPage == False):
                itemNum = len(positions['content']['result'])
            j = 0
            while (j < itemNum):
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
                print('Write a row!')
