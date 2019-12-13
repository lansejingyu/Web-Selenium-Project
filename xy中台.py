import time
from selenium import webdriver

driver =webdriver.Chrome('D:\\Chrome\\Application\\chromedriver')
# driver.maximize_window()   #浏览器最大化

# time.sleep(1.5)
driver.implicitly_wait(30)    # 隐性等待，最长等30秒

driver.get('http://192.168.2.123:3002/login')

# time.sleep(1.5)

driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').send_keys('admin')
driver.find_element_by_class_name('login100-form-btn').click()
# time.sleep(1.5)    #加等待时间，防止定位不到元素
driver.find_element_by_xpath('/html/body/div[2]/a[1]').click()
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/section/div/div[4]/div[3]/table/tbody/tr[1]/td[3]/div/a').click()

time.sleep(2)
driver.quit()