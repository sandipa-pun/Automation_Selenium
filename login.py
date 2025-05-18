from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.saucedemo.com/'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
password_field = driver.find_element(By.NAME, "password")
login_btn = driver.find_element(By.NAME, "login-button")

username_field.send_keys("standard_user")
time.sleep(1)
password_field.send_keys("secret_sauce")
time.sleep(1)
login_btn.click()

current_url = driver.current_url

if current_url == "https://www.saucedemo.com/inventory.html":
    print("login successful")

else:
    print("Login unsuccessful")

time.sleep(2)
driver.quit()