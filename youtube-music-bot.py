from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
views = int(input("enter no. of view: "))
view_time = float(input('enter time for each view: '))
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "p.webshare.io:19999"
prox.socks5_proxy = "p.webshare.io:9999"
prox.ssl_proxy = "p.webshare.io:19999"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

browser1 = webdriver.Chrome(desired_capabilities=capabilities)
browser2 = webdriver.Chrome(desired_capabilities=capabilities)
browser3 = webdriver.Chrome(desired_capabilities=capabilities)
browser4 = webdriver.Chrome(desired_capabilities=capabilities)
browser5 = webdriver.Chrome(desired_capabilities=capabilities)
browser6 = webdriver.Chrome(desired_capabilities=capabilities)

# put video link in ''
for i in range(views):
    browser1.get('')
    play_music_1 = browser1.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_1.click()
    browser2.get('')
    play_music_2 = browser2.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_2.click()
    browser3.get('')
    play_music_3 = browser3.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_3.click()
    browser4.get('')
    play_music_4 = browser4.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_4.click()
    browser5.get('')
    play_music_5 = browser5.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_5.click()
    browser6.get('')
    play_music_6 = browser6.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_6.click()
    time.sleep(view_time)

browser1.close()
browser2.close()
browser3.close()
browser4.close()
browser5.close()
browser6.close()

# script by thisisawesome1994