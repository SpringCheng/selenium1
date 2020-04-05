"""
返回所有选项
返回所有被选中的选项
通过value属性选中or取消选中选项
通过index索引选中or取消选中选项
通过标签间文本选中or取消选中选项
取消选中所有选项

@date: 2020/4/5 22:56 
@author：Spring
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(r"D:\Practice\Pycharm\Selenium\查找元素\test5.html")

# 找到select标签元素
pro = Select(driver.find_element_by_id('pro'))

# 返回所有选项
for option in pro.options:
    print(option.text)

# 返回所有被选中的选项
for option in pro.all_selected_options:
    print(option.text)

# 通过value选中
pro.select_by_value('bj')

# 通过index选中
pro.select_by_index(1)

# 通过标签文本选中
pro.select_by_visible_text("广东")

print('-------------------------------------------')
# 取消选中操作
city = Select(driver.find_element_by_id("city"))

# 全选
for option in city.options:
    if not option.is_selected():
        city.select_by_visible_text(option.text)
# 取消value取消选中
city.deselect_by_value('bj')

# 根据index取消选中
city.deselect_by_index()

# 根据标签文本选中
city.deselect_by_visible_text("武汉")

# 取消选中所有选项
city.deselect_all()
"""
取消操作只适用于添加了multiple的下拉框，否则会报错
"""
