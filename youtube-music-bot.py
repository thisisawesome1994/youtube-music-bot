from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
views = int(input("enter no. of view: "))
view_time = float(input('enter time for each view: '))
browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()

# put video link in ''
for i in range(views):
    browser1.get('')
    play_music_1 = browser1.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_1.click()
    browser2.get('')
    play_music_1 = browser2.find_element_by_xpath(""" //*[@id="contents"]/yt-button-renderer/a """)
    play_music_1.click()
    time.sleep(view_time)

browser1.close()

# script by thisisawesome1994