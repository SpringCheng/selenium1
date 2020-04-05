"""


@date: 2020/4/5 22:46 
@author：Spring
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r"D:\Practice\Pycharm\Selenium\查找元素\test4.html")

# 1、警告框
# 警告框
alert1 = driver.find_element_by_id('bu1')

# 先点击，得先弹出警告框
alert1.click()

# 切换至警告框
alert1 = driver.switch_to.alert

# 点击确定
alert1.accept()

print('-------------------------------------------------------')
# 2、确认框
alert2 = driver.find_element_by_id('bu2')
alert2.click()

# 切换至对话框
alert2 = driver.switch_to.alert

# 点击取消
alert2.dismiss()

# 点击确认
alert2.accept()

print('-------------------------------------------------------')
# 3、对话框
alert3 = driver.find_element_by_id('bu3')
alert3.click()

# 切换至对话框
alert3 = driver.switch_to.alert

# 输入值到对话框中
alert3.send_keys("输入对话框")

# 点击确认
alert3.accept()
