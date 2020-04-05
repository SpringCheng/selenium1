"""
删除键
空格键
制表键
回退键
回车键
全选
复制
剪切
粘贴
F1-F12
......其实就是所有键盘都能模拟，包括alt、shift、insert、delete、home等等等...易懂

@date: 2020/4/5 17:16 
@author：Spring
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

inputElement=driver.find_element_by_id('kw')
inputElement.send_keys('python自动化测试')
# 全选
inputElement.send_keys(Keys.CONTROL,'a')

# 复制输入框内容
inputElement.send_keys(Keys.CONTROL,'c')

# 剪切输入框内容
inputElement.send_keys(Keys.CONTROL,'x')

# 粘贴输入框内容
inputElement.send_keys(Keys.CONTROL,'v')

# 空格键
inputElement.send_keys(Keys.SPACE)

# 后退键
inputElement.send_keys(Keys.BACK_SPACE)

# tab键
inputElement.send_keys(Keys.TAB)

# 回车键
inputElement.send_keys(Keys.ENTER)

# 刷新页面
inputElement.send_keys(Keys.F5)

