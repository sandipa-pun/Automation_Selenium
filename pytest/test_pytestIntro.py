from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(scope="module")

def browser(): #initialize browser
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_website(browser):
    url = "https://www.google.com"
    browser.get(url)
    browser.maximize_window()
    assert "Google" in browser.title, f"Expected 'Google' but got '{browser.title}'"
    time.sleep(3)


def test_youtube(browser):
    url = "https://www.youtube.com"
    browser.get(url)
    browser.maximize_window()
    assert "YouTube" in browser.title, f"Expected 'YouTube' but got '{browser.title}'"
    time.sleep(3)

# pytest test_intro.py::test_youtube
