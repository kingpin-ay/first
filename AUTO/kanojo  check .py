from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import mouse_button
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


browser = webdriver.Chrome()
browser.maximize_window()
wait = WebDriverWait(browser, 10)
# sleep(1)
browser.get("http://mangahere.win/")
# sleep(1)
# advertisment_cancle_button = browser.find_element_by_xpath("//*[@id='AdskeeperC992642Popup-close-btn']/img")
# ads = advertisment_cancle_button.is_displayed()
"""
if ads == true :
    advertisment_cancle_button.click()
    print('advertiserment is removed good to go ....!!')
"""
search_box = browser.find_element_by_class_name("searchi")

search_box.send_keys("Kanojo")
sleep(2)
kanojo_okarishimasu =browser.find_element_by_xpath("//*[@id='3585']/div")

print(f'kanojo button is appeared : ' + str(kanojo_okarishimasu.is_displayed()))

print(f'kanojo button is enabled : ' + str(kanojo_okarishimasu.is_enabled()))
kanojo_okarishimasu.click()

chart_list = browser.find_element(By.XPATH, "//*[@id='chapter']/div/div[2]/div[1]/span[1]/a")

print(f'if chart list  is appeared : '+ str(chart_list.is_displayed()))
print(f'chart list button is enabled : ' + str(chart_list.is_enabled()))
# if yeah == "true":
chart_list.click()

try:
    wait.until(ec.element_to_be_clickable(
        browser.find_element_by_xpath("//*[@id='AdskeeperC992642Popup-close-btn']/img")))
    ads_cut_button = browser.find_element_by_xpath("//*[@id='AdskeeperC992642Popup-close-btn']/img")
    print(f'ads button is appeared : ' + str(ads_cut_button.is_displayed()))
    print(f'ads button is enabled : '+ str(ads_cut_button.is_enabled()))
    ads_cut_button.click()
except Exception as e:
    print(e)

