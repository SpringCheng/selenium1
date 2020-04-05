"""
执行操作  perform()
左键、右键单击、双击 click() context_click() double_click()
鼠标悬停到元素、偏移处 move_to_element move_to_element_with_offset
长按  click_and_hold
拖动  drag_and_drop

@date: 2020/4/5 16:52 
@author：Spring
"""

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# 1 perform()方法
# 主要是调用其他操作方法后，都要再次调用这个方法，表示执行某个鼠标操作，后面会有例子
# 创建实例
chains = ActionChains(driver)

# 访问网址
driver.get(r"D:\Practice\Pycharm\Selenium\查找元素\test2.html")
# 登录按钮
username = driver.find_element_by_id("username")
login_btn = driver.find_element_by_class_name("login")
password = driver.find_element_by_id("password")
# 左键点击
chains.click(username).perform()
# 右键点击
chains.context_click(username).perform()
# 双击
chains.double_click(password).perform()

print('----------------------------------------------------------')
# 2 鼠标悬停到元素、偏移处
# 悬停到设置按钮
chains.move_to_element(login_btn).perform()
# 悬停到指定平移量
# move_to_element_with_offset() 是先找到元素，再根据元素位置偏移指定偏移量
chains.move_to_element_with_offset(login_btn, 2, 2).perform()

print('----------------------------------------------------------')
# 3 长按
chains.click_and_hold(login_btn).perform()

print('----------------------------------------------------------')
# 4 拖动
"""
drag_and_drop 将源元素拖动到目标元素处
drag_and_drop_by_offset 将源元素拖动指定偏移量
"""
chains.drag_and_drop(source=username, target=password)
chains.drag_and_drop_by_offset(source=username, xoffset=20, yoffset=20)

