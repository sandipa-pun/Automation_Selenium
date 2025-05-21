# https://demoqa.com/nestedframes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(scope="module")

def browser(): #initialize browser
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_frames(browser):
    url = "https://demoqa.com/nestedframes"
    browser.get(url)
    time.sleep(2)

    parent = browser.find_element(By.XPATH, '//*[@id="frame1"]')
    browser.switch_to.frame(parent)

    parent_content = browser.find_element(By.TAG_NAME, "body").text
    print(f"The parent content is {parent_content}")

    child = browser.find_element(By.XPATH, '/html/body/iframe')
    browser.switch_to.frame(child)

    child_content = browser.find_element(By.TAG_NAME, "p").text
    print(f"The child content is {child_content}")