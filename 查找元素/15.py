"""


@date: 2020/4/6 0:17 
@author：Spring
"""

from time import sleep

from selenium import webdriver

# 需要将驱动路径改成自己的路径哦
driver = webdriver.Chrome()

url = "https://m.weibo.cn/"

driver.get(url)

# 点击搜索框
driver.find_element_by_class_name("m-search").click()

sleep(2)

# 点击【微博实时搜索】
driver.find_element_by_class_name("card-main").find_elements_by_class_name("m-item-box")[-1].click()

sleep(2)

# 查找list
lists = driver.find_element_by_class_name("card11").find_element_by_class_name("card-list").find_elements_by_class_name("card4")
# print(list(lists))
# 循环热搜列表
for i in lists:
    text = i.find_element_by_class_name("main-text").text
    span = i.find_elements_by_class_name("m-link-icon")
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