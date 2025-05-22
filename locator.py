from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.thirdeyeadventure.com')
driver.maximize_window()
time.sleep(2)

scroll_speed = 300
max_scrolls = 50

for _ in range(max_scrolls):
    try:
        element = driver.find_element(By.CLASS_NAME, "title-content__wrpper")

       
        is_visible = driver.execute_script("""
            const rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)
            );
        """, element)

        if is_visible:
            print("Element is now visible in viewport. Stopping scroll.")
            break

    except:
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(1)

time.sleep(3)
driver.quit()
