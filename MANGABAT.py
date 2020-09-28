from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# browser.maximize_window()
browser.get("https://m.mangabat.com/hp")  # browser is open and site has reached
sleep(2)

login_button = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/a[1]')
# wait = WebDriverWait(browser, 7)
# element = wait.until(ec.element_to_be_clickable(login_button))
login_button.click()

sleep(2)

user_name = browser.find_element_by_name('username')
user_name.send_keys('a954710')

password = browser.find_element_by_name('password')
password.send_keys('ayush0075050')

captcha = int(input('please enter the captcha : '))
captcha_button = browser.find_element_by_name('captchar')
captcha_button.send_keys(captcha)


submit_button = browser.find_element_by_name('submit_login')
submit_button.click()
