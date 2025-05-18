
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.thirdeyeadventure.com')
driver.maximize_window()
time.sleep(2)

page_height = driver.execute_script("return document.body.scrollHeight")
scroll_speed = 500
scroll_iteration = int(page_height/scroll_speed)

for _ in range(scroll_iteration):
    try:
        element = driver.find_element(By.CLASS_NAME, "title-content__wrapper")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        break 
    except:
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(1)

time.sleep(3)
driver.quit()
