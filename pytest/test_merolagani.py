from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture(scope="module")

# Initialize Browser
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

    #Alert
    try:
        browser.switch_to.alert.accept()
        time.sleep(2)
    except:
        pass

    liveTrading = browser.find_element(By.XPATH, '//*[@id="navbar"]/ul[1]/li[2]/ul/li[1]/a')
    liveTrading.click()
    time.sleep(3)


    #Scroll
    browser.execute_script("window.scrollBy(0,400);")
    time.sleep(3)

    trading = browser.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LiveTrading"]')
    browser.execute_script("arguments[0].scrollTop = 1000", trading)
    time.sleep(2)

    # select
    companies = browser.find_elements(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LiveTrading"]/table/tbody/tr/td[1]/a')
    company = companies[0]
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", company)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_LiveTrading"]/table/tbody/tr[1]/td[1]/a')))
    company.click()
    time.sleep(2)

    #Alert
    try:
        browser.switch_to.alert.accept()
        time.sleep(2)
    except:
        pass

    # new tab

    browser.switch_to.window(browser.window_handles[1])  # Move to the new tab
    time.sleep(2)

    # price history
    page_height = browser.execute_script("return document.body.scrollHeight")
    scroll_speed = 500
    scroll_iteration = int(page_height/scroll_speed)

    for _ in range(scroll_iteration):
        try:
            history = browser.find_element(By.ID, 'ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab')
            browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", history)
            time.sleep(1)
            history.click()
            break
        except:
            browser.execute_script("window.scrollBy(0, 500);")
            time.sleep(1) 

    time.sleep(2)


    #Alert
    try:
        browser.switch_to.alert.accept()
        time.sleep(2)
    except:
        pass

    
    # date
    date = browser.find_element(*(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']"))
    # date = browser.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter"]')
    date.send_keys("05/21/2025")
    time.sleep(2)

    search = browser.find_element(By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lbtnSearchPriceHistory']")
    search.click()

    time.sleep(10)




