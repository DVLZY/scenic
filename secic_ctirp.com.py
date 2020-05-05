import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

# 初始化
driver = webdriver.Chrome()                 # 引入chrome驱动
# driver.get('https://you.ctrip.com/sitemap/spotdis/c0')     # 打开目标网址

def url(url,re_rule):
    driver.get(url)
    lastPage = driver.find_element_by_xpath('//b[@class="numpage"]').text # 65
    for i in range(1,lastPage+1):
        urli = "https://you.ctrip.com/sight/guilin28/s0-p"+str(i)+".html"
        driver.get(urli)
        name_list = driver.find_elements_by_xpath(re_rule)
        time.sleep(0.5)
        for name in name_list:
            print(name.text)

url0 = "https://you.ctrip.com/sight/guilin28/s0-p1.html"
re_rule0 = '//div[@class="rdetailbox"]/dl/dt/a'
url(url0,re_rule0)

