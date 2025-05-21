# https://demoqa.com/alerts

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(scope="module")

def browser(): #initialize browser
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_alert(browser):
    url = "https://demoqa.com/alerts"
    browser.get(url)
    browser.maximize_window()
    # time.sleep(2)

    alert_btn = browser.find_element(*(By.XPATH,"//button[@id='alertButton']"))
    alert_btn.click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    time.sleep(2)