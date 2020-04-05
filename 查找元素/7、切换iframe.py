"""


@date: 2020/4/5 18:08 
@author：Spring
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('test3.html')
driver.maximize_window()

# 找到iframe元素
iframe1 = driver.find_element_by_id('iframe1')

# 切换到iframe1
driver.switch_to.frame(iframe1)
# 切换的方法2
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it('iframe'))
# 找到iframe中的元素 找到搜索框
driver.find_element_by_id('kw').send_keys('python', Keys.ENTER)

# 切换到主界面
driver.switch_to.default_content()
