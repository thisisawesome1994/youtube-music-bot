from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
import time
views = int(input("enter no. of view: "))
view_time = float(input('enter time for each view: '))

# put video link in ''
for i in range(views):
    f = open('links.txt', 'r', encoding='utf-8')
    for line in f:
        url = line
    f = open('proxies.txt', 'r', encoding='utf-8')
    for line in f:
        proxy = line
    f = open('username.txt', 'r', encoding='utf-8')
    for line in f:
        username = line
    f = open('password.txt', 'r', encoding='utf-8')
    for line in f:
        password = line
    f = open('useragents.txt', 'r', encoding='utf-8')
    for line in f:
        useragent = line
    opts1 = Options()
    opts1.add_argument('--user-agent=%s'% useragent)
    #opts1.add_argument('--mute-audio')
    opts1.add_argument('--incognito')
    opts1.add_argument('--proxy-server=%s'% proxy)
    #opts1.add_argument('--headless')
    opts1.add_argument('--start-maximized')
    browser1 = webdriver.Chrome(options=opts1)
    browser1.execute_script("window.location.replace(arguments[0])", url)
    time.sleep(10)
    play_music_1 = browser1.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_1.click()
    time.sleep(view_time)
    browser1.quit()
# script by thisisawesome1994