from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = 'https://formy-project.herokuapp.com/form'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

time.sleep(2)

first_name_field = driver.find_element(By.XPATH,"//input[@id='first-name']")
first_name_field.send_keys("John")


last_name_fiels = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_fiels.send_keys("Doe")


job  = driver.find_element(By.XPATH, "//input[@id='job-title']")
job.send_keys("QA Engineer")


education_btn = driver.find_element(By.XPATH, "//input[@id='radio-button-3']")
education_btn.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,1000);")
time.sleep(1)

multi_choice_btn1 = driver.find_element(By.XPATH,"//input[@id='checkbox-2']")
multi_choice_btn2 = driver.find_element(By.XPATH,"//input[@id='checkbox-3']")
multi_choice_btn1.click()
multi_choice_btn2.click()
time.sleep(2)

# drop_down = driver.find_element(By.XPATH, "//select[@id='select-menu']")
# drop_down.click()
# option = driver.find_element(By.XPATH, '//*[@id="select-menu"]/option[2]')
# option.click()
# time.sleep(2)

element = driver.find_element(By.XPATH, "//select[@id='select-menu']")
select = Select(element)
select.select_by_index(2)

# date = driver.find_element(By.XPATH, "//input[@id='datepicker'']")
date = driver.find_element(By.ID, "datepicker")
date.send_keys("05/10/2025")

time.sleep(2)
submit = driver.find_element(By.XPATH, "//a[normalize-space()='Submit']")
submit.click()

time.sleep(5)
driver.quit()
 
