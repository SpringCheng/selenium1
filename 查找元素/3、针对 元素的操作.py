"""

点击
输入内容、清除内容
返回元素尺寸、坐标
获取元素标签文本
获取元素属性值
检查元素：是否可见、是否可点击、是否已被选择
表单提交

@date: 2020/4/5 16:26 
@author：Spring
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(r"D:\Practice\Pycharm\Selenium\查找元素\test2.html")

# # 1  点击
# loging_btn = driver.find_elements_by_class_name('login')
# loging_btn.click()

print('-------------------------------------------------------')
# 2 输入内容 、清除内容
username = driver.find_element_by_id("username")
# 输入内容
username.send_keys("zhangsan")
sleep(5)
# 清除内容
username.clear()
print('-------------------------------------------------------')

# 3 返回元素尺寸坐标
login_btn = driver.find_elements_by_class_name('lgoin')
# 打印元素宽高
print(f"元素宽高：{login_btn.size}")
# 打印元素 x y轴值
print(f"元素坐标值：{login_btn.location}")

print('-------------------------------------------------------')
# 4 获取元素标签文本
a_text = driver.find_element_by_tag_name("a")
print(a_text.text)

# 获取第一个标签为div的文本
div_text = driver.find_element_by_tag_name('div')
print(div_text.text)
"""
.text 返回的是标签里面的文本，如 <html>内容....</html> ，返回的则是中间那些内容
如果标签内还有子标签，那也只会获取子标签的文本内容，不会获取标签，像上面获取div的text一样
"""

print('-------------------------------------------------------')
# 5 获取元素的属性值
# 获取元素属性值
a_attr = driver.find_element_by_class_name("mnav")
print(a_attr.get_attribute("href"))

print('-------------------------------------------------------')
# 6 检查元素：是否可见，是否可点击，是否已被选择
# 找到 不可见元素
ant_btn3 = driver.find_element_by_class_name("ant-btn3")
# 找到 可见元素
ant_btn4 = driver.find_element_by_class_name("ant-btn4")

# 查看是否可见
print("不可见元素:", ant_btn3.is_displayed())
print("可见元素:", ant_btn4.is_displayed())

# 找到 不可点击元素
ant_btn3 = driver.find_element_by_class_name("ant-btn1")
# 找到 可点击元素
ant_btn4 = driver.find_element_by_class_name("ant-btn2")

# 查看是否可点击
print("不可点击元素:", ant_btn3.is_enabled())
print("可点击元素:", ant_btn4.is_enabled())

# 找到 未被选中的元素
option1 = driver.find_elements_by_tag_name("option")[0]
# 找到 已被选中的元素
option2 = driver.find_elements_by_tag_name("option")[-1]

# 查看是否被选择
print("未被选择元素:", option1.is_selected())
print("已被选择元素:", option2.is_selected())

print('-------------------------------------------------------')
# 7 表单提交
driver.get("https://www.baidu.com")

# 找到搜索框
search_text = driver.find_element_by_id('kw')

# 输入搜索内容
search_text.send_keys('小菠萝测试笔记')

# 提交表单
search_text.submit()
search_text.send_keys('小萝莉笔记', Keys.ENTER)
