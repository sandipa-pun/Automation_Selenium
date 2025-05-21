from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture(scope="module")


def browser():
    driver= webdriver.Chrome()
    yield driver
    driver.quit()


def test_livetrading(browser):
    url = "https://merolagani.com"
    browser.get(url)
    browser.maximize_window()
    time.sleep(3)
    wait = WebDriverWait(browser, 10)

    Market = browser.find_element(By.XPATH, '//*[@id="navbar"]/ul[1]/li[2]/a')
    Market.click()
    time.sleep(2)

    try:
        browser.switch_to.alert.dismiss()
        time.sleep(2)
    except:
        pass

    liveTrading = browser.find_element(By.XPATH, '//*[@id="navbar"]/ul[1]/li[2]/ul/li[1]/a')
    liveTrading.click()
    time.sleep(3)

    browser.execute_script("window.scrollBy(0,400);")
    time.sleep(3)

    # frame_livetrading = browser.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LiveTrading"]')
    # browser.switch_to.frame(frame_livetrading)
    # browser.execute_script("window.scrollBy(0,500);")
    # time.sleep(3)

    try:
        frame = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_LiveTrading")))
        browser.switch_to.frame(frame)
    except Exception as e:
        pytest.fail(f"Unable to switch to frame: {e}")

    # Scroll inside the iframe
    browser.execute_script("window.scrollBy(0, 500);")
    








