from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

url = 'https://filebin.net/'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
time.sleep(2)

file = driver.find_element(By.XPATH,'//*[@id="fileField"]')
file.send_keys("C:/Users/sandi/Downloads/soft_logo.jpg")
time.sleep(2)

more = driver.find_element(By.XPATH, "//a[@id='dropdownFileMenuButton']")
more.click()
option = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[5]/div/div/a[1]')
option.click()
proceed = driver.find_element(By.XPATH, '/html/body/div[3]/p/a[2]')
proceed.click()

# select = Select(element)
# select.select_by_index(1)


time.sleep(5)
driver.quit()

