import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

driver = webdriver.Chrome()                 # 引入chrome驱动
driver.get('http://www.bytravel.cn/')     # 打开目标网址

def url(url,re_rule):
    driver.get(url)
    name_list = driver.find_elements_by_xpath(re_rule)
    time.sleep(0.5)
    for name in name_list:
        print(name.text)

url0 = "http://www.bytravel.cn/view/index128_list.html"
re_rule0 = '//div[@id="tctitle"]/a'
url(url0,re_rule0)

for i in range(1,20):
    urli = "http://www.bytravel.cn/view/index128_list"+ str(i) +".html"
    url(urli,re_rule0)