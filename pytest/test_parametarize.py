# https://www.saucedemo.com/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(scope="module")

def browser(): #initialize browser
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password",[
    ("standard_user", "secret_sauce"), #success
    ("locked_out_user", "secret_sauce"), #failed
    ("problem_user", "secret_sauce") #success
    ])

def test_login(browser,username,password):
    url = "https://www.saucedemo.com"
    browser.get(url)
    browser.maximize_window()
    time.sleep(2)

    username_field = browser.find_element(By.XPATH, "//input[@id='user-name']")
    password_field = browser.find_element(By.XPATH, "//input[@id='password']")
    login_btn = browser.find_element(By.XPATH, "//input[@id='login-button']")

    username_field.send_keys(username)
    time.sleep(2)
    password_field.send_keys(password)
    time.sleep(2)
    login_btn.click()
    time.sleep(2)

    try:
        browser.switch_to.alert.accept()
        print("Login success")
    except Exception as e:
        page_src = browser.page_source
        assert "Products" in page_src
        print(f"Login failed {e}")