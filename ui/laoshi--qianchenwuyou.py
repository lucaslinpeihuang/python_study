# -*-coding:UTF-8 -*-
from selenium import webdriver
from xlrd import open_workbook
from xlutils.copy import copy
from time import sleep

#一、登录
# 一、先  webdriver：引出包，再进行下一步操作
#   ..\drivers\chromedriver.exe：返回到drivers包下的chromedriver.exe
#找到网址，跟踪进去
driver = webdriver.Chrome('..\drivers\chromedriver.exe')
#找到网址，跟踪进去
driver.get('https://login.51job.com/login.php')
#最大化这个网址
driver.maximize_window()
#二、登录前程无忧----在网址上写入账户和密码
#点击右键-检查可看到id="loginname
driver.find_element_by_id('loginname').send_keys('19922356265')
#点击右键-检查可看到id="password
driver.find_element_by_id('password').send_keys('wangwei.811')
#不用键盘登录
driver.find_element_by_id('login_btn').click()

#二、职位搜索，职位写入：软件测试工程师
#↓右击--检查--里有a链接，需要用以下格式：.find_element_by_link_text
driver.find_element_by_link_text('职位搜索').click()
#点击：要写入的值（空行）--点击检查，send_keys：填入需搜索的值
driver.find_element_by_id('keywordInput').send_keys('软件测试工程师')
#点击搜索，右击检查，出现search_btn，写入在下面↓
driver.find_element_by_id('search_btn').click()

#print(driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]/div[2]/a'))


sleep(2)
#点击全选，右击检查，出现了chall，代表搜索完之后进行全选
driver.find_element_by_class_name('chall').click()

#四、取出公司信息，用i值来循环取每个值
company = []

for i in range(1, 51):
# ↓  /html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]/div[2]/a
# ↓  /html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[2]/div[2]/a
#    /html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[%d]/div[2]/a' %i   里的%d是对上面倒数第二个的div1、2进行修改，%i是对%d循环
#append：执行company这个数据
    company.append(driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[%d]/div[2]/a' %i).text)
print(company)
#↑打印出（公司信息的所有值）/html/body/div[2]/div[3]/div/div[2]/div[4]/div[1]/div[1]/div[2]/a

#五、在表格里写入数据进去

#打开d:\emp.xls表格
yuanshi_excel = open_workbook(r'd:\emp.xls',formatting_info=True)
#取d:\emp.xls，sheet（黑名单公司）表（可有两种写法）
sheet = yuanshi_excel.sheet_by_name('黑名单公司')

black_company = sheet.col_values(0,1)
print(black_company)


#复制yuanshi_excel（原始表），新建一个new_excel（新表)
new_excel = copy(yuanshi_excel)
#取d:\emp.xls，第三个：sheet（公司信息表）
sheet = new_excel.get_sheet(3)
#循环上面company = []的值
for i in range(len(company)):
#表格里写入company = []的值
#               i+1代表除掉开头：公司信息这一栏，（列）
#                0代表：表格里的A行，（行）     
#                company[i]代表：公司信息
    sheet.write(i+1,0,company[i])
    
    
#六、保存
new_excel.save(r'd:\caichang.xls')