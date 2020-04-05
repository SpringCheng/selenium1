"""


@date: 2020/4/5 23:42 
@author：Spring
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://m.weibo.cn/')

# 点击搜索框
driver.find_element_by_class_name('m-search').click()

time.sleep(1)

# 点击微博热搜榜
driver.find_element_by_xpath("//*[@id='app']/div[1]/div[1]/div[2]/div/div/div[8]/div/div").click()

# 查找list
# lists = driver.find_element_by_xpath("//div[@class='card-list']//div[@class='card m-panel card4']
lists = driver.find_element_by_class_name('card11').find_element_by_class_name('card-list').find_elements_by_class_name('card4')
lists = driver.find_element_by_class_name("card11").find_element_by_class_name("card-list").find_elements_by_class_name("card4")
# print(lists)

# 循环热搜列表
for i in lists:
    text = i.find_element_by_class_name("main-text m-text-cut").text
    span = i.find_element_by_class_name("m-link-icon")
    if span:
        src = span[0].find_element_by_tag_name("img").get_attribute("src")

        if "hot" in src:
            print(f"{text} 是 很热的头条")
        elif "new" in src:
            print(f"{text} 是 新的头条")
        elif "fei" in src:
            print(f"{text} 是 沸腾的头条")
        elif "recom" in src:
            print(f"{text} 是 推荐的头条")
        else:
            print(f"{text} 是 普通的头条")
