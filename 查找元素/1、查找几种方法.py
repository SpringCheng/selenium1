"""
在前端，一般多个元素共用一个class
但 find_element_by_class_name 只返回第一个匹配到class的元素
坏处：当找不到元素则报错



@date: 2020/4/5 15:46 
@author：Spring
"""

from selenium import webdriver

# 加载驱动
driver = webdriver.Chrome()

# 访问页面
driver.get(r"D:\Practice\Pycharm\Selenium\查找元素\test.html")

# 1 ****通过id查找*****
# 找到id=username元素
username = driver.find_element_by_id('username')

# 输入值 张三
username.send_keys('张三')

# 找到id=password元素
password = driver.find_element_by_id('password')

# 输入值123456
password.send_keys(123456)

print('------------------------------------------')
# 2 ****通过class值查找（仅返回匹配到的第一个值）****
login_btn = driver.find_element_by_class_name('login')

# =====找到所有class=li的元素
lis = driver.find_elements_by_class_name("li")
for i in lis:
    print(i.text)

# 点击
login_btn.click()
"""
查找所有class等于li的元素
返回的是一个元素列表，若只匹配到一个也是列表
好处：当没有找到元素时不会报错，而是返回空列表 []
"""


lis = driver.find_elements_by_class_name('li')
for i in lis:
    print(i.text)

print('------------------------------------------')
# 3 ****通过name查找****
password = driver.find_element_by_name('password')
password.send_keys('123')

"""
和class一样，也有可能有多个元素共用一个name
但  find_element_by_name  只返回第一个匹配到name的元素
想返回多个的话，和class一样，需要调用 find_elements_by_name 方法，这里不再赘述，写法和上面一致
"""

print('------------------------------------------')
# 4 *****通过标签查找****
# =====通过 元素标签（仅返回匹配到的第一个）=====
p = driver.find_element_by_tag_name("p")
# 打印元素的文本值
print(p.text)

print("===")
# =====通过 元素标签（返回匹配到的所有元素）=====
ps = driver.find_elements_by_tag_name("p")
for p in ps:
    print(p.text)

"""
多个元素同种HTML标签见怪不怪了
同样的， find_element_by_tag_name 返回第一个匹配到标签的元素
 find_elements_by_tag_name 可以返回所有匹配到标签的元素
"""

print('------------------------------------------')

# 5 通过超链接文本查找
# =====通过 超链接的文本查找元素（仅支持精确匹配）
atext = driver.find_element_by_link_text("抗击肺炎")
print(atext.text)

print("===")
ass = driver.find_elements_by_link_text("抗击肺炎")
for i in ass:
    print(i.text)

print('------------------------------------------')

# 6 通过超链接文本（模糊匹配）
# =====通过 超链接的文本查找元素（支持模糊匹配）
atext = driver.find_element_by_partial_link_text("肺炎")
print(atext.text)

print("===")
ass = driver.find_elements_by_partial_link_text("肺炎")
for i in ass:
    print(i.text)

print('------------------------------------------')
# 7 通过xpath查找
# ====通过 xpath
lis = driver.find_element_by_xpath("/html/body/div/ul[2]/li[1]")
print(lis.text)

"""
常用的xpat写法
dr.find_element_by_xpath("//*[@id='kw']")
dr.find_element_by_xpath("//*[@name='wd']")
dr.find_element_by_xpath("//input[@class='s_ipt']")
dr.find_element_by_xpath("/html/body/form/span/input")
dr.find_element_by_xpath("//span[@class='soutu-btn']/input")
dr.find_element_by_xpath("//form[@id='form']/span/input")
dr.find_element_by_xpath("//input[@id='kw' and @name='wd']")
"""

print('------------------------------------------')
# 8 通过css选择器查找
# ====通过css选择器
lis = driver.find_element_by_css_selector("body > div > ul > li:nth-child(2)")
print(lis.text)

