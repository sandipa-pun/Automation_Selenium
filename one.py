from selenium import webdriver
# from selenium.webdriver.chrome.service import service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.edge.service import service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

#driver installation

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver = webdriver.Chrome()

#provide website

url = "https://merolagani.com"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(3)

driver.quit()