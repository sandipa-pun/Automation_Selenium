from selenium import webdriver
import time

url = 'https://www.thirdeyeadventure.com'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

# scoll

# driver.execute_script("window.scrollBy(0,10000);")

page_height = driver.execute_script("return document.body.scrollHeight")

scroll_speed = 500

scroll_iteration = int(page_height/scroll_speed)

for _ in range(scroll_iteration):
    driver.execute_script("window.scrollBy(0,300);")
    time.sleep(1)

# time.sleep(3)

driver.quit() 

