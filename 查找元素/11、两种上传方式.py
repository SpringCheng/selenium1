"""


@date: 2020/4/5 23:14 
@author：Spring
"""
import time
from pathlib import Path

from selenium import webdriver
driver = webdriver.Chrome()
# 1、input标签上传文件
driver.get(r"D:\Practice\Pycharm\Selenium\查找元素\test6.html")

# 定位上传文件元素input
pic=driver.find_element_by_id('pic')

# 上传文件
pic.send_keys(r"D:\Practice\Pycharm\Selenium\查找元素\test.html")

# 2、非input标签上传文件
# driver.get("https://tinypng.com/")
# paths=Path.cwd().parent
#
# # 触发文件上传操作
# driver.find_element_by_css_selector('section.target').click()
# time.sleep(2)
#
# # 一级顶层窗口
# dialog = win32gui.FindWindow("#32770", "打开")
#
# # 二级窗口
# comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
#
# # 三级窗口
# comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, "ComboBox", None)
#
# # 四级窗口 -- 文件路径输入区域
# edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)
#
# # 二级窗口 -- 打开按钮
# button = win32gui.FindWindowEx(dialog, 0, "Button", None)
#
# # 1、输入文件路径
# filepath = f"{paths}\\resources\\11.png"
# win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)
#
# # 2、点击打开按钮
# win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)