"""


@date: 2020/4/5 17:46 
@author：Spring
"""
# 1、强制等待
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
sleep(4)

# 2、隐式等待
"""
如果在规定时间内，整个网页加载完，则执行下一步，否则会抛出异常
"""

# 调用一个implicitly_wait()方法
driver.implicitly_wait(10)

# 访问网页
driver.get('https://www.baidu.com')

# 3、显示等待
"""
相比隐式等待，显式等待只对指定元素生效，不再是在整个WebDriver生命周期内生效【仅对元素生效】

可以根据需要定位的元素来设置显式等待，无需等待页面完全加载，节省大量因加载无关紧要文件而浪费
掉的时间【针对元素设置，无需等待页面加载完成，节省加载时间】

WebDriverWait(driver实例, 超时时长, 调用频率, 忽略的异常).until(要调用的方法, 超时时返回的信息) 
until(self, method, message='')  抛出异常时的文案，会返回 TimeoutException ，表示超时
"""
# 设置元素等待实例，最多等10秒，每0.5秒查看条件是否成立
element = WebDriverWait(driver, 10, 0.5).until(
    # 条件：直到元素加载完成
    EC.presence_of_element_located((By.ID, 'kw'))
)
