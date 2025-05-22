
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from pages.login_page import LoginPage
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture()

def driver(): #initialize browser
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    loginpage = LoginPage(driver)
    url = "https://www.saucedemo.com/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    loginpage.enter_username("standard_user")
    time.sleep(1)

    loginpage.enter_password("secret_sauce")
    time.sleep(1)

    loginpage.click_login()
    time.sleep(1)