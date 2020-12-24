# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from pymysql import connect
from selenium.webdriver.remote import switch_to


# webdriver为包包下的chrome（）括号里面填
driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/')
driver.maximize_window()

# 通过id定位元素：find_element_by_id("id_vaule")
# 通过name定位元素：find_element_by_name("name_vaule")
# 通过tag_name定位元素：find_element_by_tag_name("tag_name_vaule")
# 通过class_name定位元素：find_element_by_class_name("class_name")
# 通过css定位元素：find_element_by_css_selector()
# 通过xpath定位元素：find_element_by_xpath("xpath")

# 填写账号密码的方式点击登陆
# find_element_by_name定位元素用，send_keys写入文字的方式
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
# driver.find_element_by_class_name('btn-a').click() 
# 第一种方法点击登录器的方法，第二种↓下面这个是用xpath的方法
# click()为点击登陆
driver.find_element_by_xpath('//*[@id="loginPanel"]/div[3]/input').click()

# sleep为等待加载时间如下
sleep(1)
# switch_to只要是带a超链接就要用进入，frame为分支（一体）
driver.switch_to.frame('main-frame')
driver.find_element_by_xpath('//*[@id="menu-ul"]/li[2]/ul/li[1]/a').click()
# 除了用switch_to之外也能用xpath
driver.find_element_by_link_text('商品列表').click()
# 切换到当前主页面的意思switch_to.default_content()
driver.switch_to.default_content()
# 再进去右侧管理页面
driver.switch_to.frame('main-frame')

sleep(2)
# find_element_by_name定位元素用，send_keys写入文字的方式
driver.find_element_by_name('keyword').send_keys('车')
# driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()
# driver.find_element_by_class_name('button').click()
driver.find_element_by_xpath('/html/body/div[3]/form/input[2]').click()
# ↑三种方式都行


# ↓三种定位元素样式
#driver.find_element_by_css_selector('.caichang')
#driver.find_element_by_tag_name(name)
#//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span
sleep(1)

search_text = driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
search_total = driver.find_element_by_id('totalRecords').text
# print(search_total)
# print(type(search_total))
conn  = connect('192.168.1.4','root','root','ecshop',3306)
cursor = conn.cursor()
cursor.execute("select goods_name from ecs_goods where goods_name like '%车%'")
#                      ↑是select（找数据库内容） ename form(找表) emp where（条件） depton=20

rs = cursor.fetchall()
# print(rs)

cursor.execute("select count(*) from ecs_goods where goods_name like '%车%'")
total = cursor.fetchone()
# print(total)
# print(type(total[0]))
if search_text==rs[0][0] and int(search_total) ==total[0] :
    print('测试通过')
else:
    print("测试不通过")
cursor.close()
conn.close()

