"""


@date: 2020/4/5 15:31 
@author：Spring
"""

from selenium import webdriver
import time

# 加载浏览器驱动
driver = webdriver.Chrome()

# 访问网址
driver.get('https://www.baidu.com')

# 找到搜索框
inputElement = driver.find_element_by_id('kw')

# 输入搜索内容
inputElement.send_keys('python自动化')

# 找到搜索按钮
searchElement = driver.find_element_by_id('su')

# 点击搜索按钮
searchElement.click()

# 等待页面加载完
time.sleep(3)

# 释放资源，退出浏览器
driver.quit()
