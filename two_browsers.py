from selenium import webdriver
import time

url = 'https://www.thirdeyeadventure.com'

browser_arr = ['Chrome', 'Edge']

for browser in browser_arr:
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == "Edge":
        driver = webdriver.Edge()
    else: 
        continue

    driver.get(url)
    driver.maximize_window()
    print("Time: ", driver.title)
    time.sleep(3)
    driver.quit()