import re
import requests
import pytesseract
import time
from selenium import webdriver
from PIL import Image,ImageEnhance
from collections import defaultdict

driver =webdriver.Chrome('D:\\Chrome\\Application\\chromedriver')

driver.get('http://mall.test.xyb2b.com.cn/login')

# time.sleep(3)
# driver.maximize_window()   #浏览器窗口最大化
# driver.implicitly_wait(30) # 隐性等待，最长等30秒

# driver.find_element_by_tag_name("input").send_keys("570820332@qq.com")
# driver.find_element_by_tag_name('input').send_keys("111111qqqqqq")
driver.find_elements_by_class_name('el-input__inner')[0].send_keys("18067921639")   #用户名输入
driver.find_elements_by_class_name('el-input__inner')[1].send_keys("123456")             #密码输入
# driver.find_elements_by_class_name('ivu-input')[2].send_keys('123')              #验证码输入

time.sleep(5)

driver.find_element_by_class_name('ivu-btn').click()          #登录

time.sleep(3)    #加等待时间，防止定位不到元素

# driver.find_elements_by_class_name('header-title')[2].click()   #佣金列表
driver.find_elements_by_class_name('header-title')[1].click()   #资金管理

time.sleep(3)

driver.find_elements_by_class_name('ivu-icon-ios-arrow-down')[3].click()  #业务类型
driver.find_elements_by_class_name('ivu-select-item')[8].click()          #选择拒绝
driver.find_element_by_class_name('gQueryBtn').click()                    #查询