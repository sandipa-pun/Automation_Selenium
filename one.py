from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.common.by import By
=======
>>>>>>> 00d42342092d210e860dccbe87d780b55c20093a
# from selenium.webdriver.chrome.service import service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.edge.service import service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

#driver installation

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

<<<<<<< HEAD
browser = webdriver.Chrome()

# #provide website

# url = "https://merolagani.com"

# driver.get(url)
# driver.maximize_window()
# title = driver.title
# print(title)
# time.sleep(3)

# driver.quit()
url = "https://demoqa.com/nestedframes"
browser.get(url)
iframe = browser.find_element(By.XPATH, "//body")
browser.switch_to.frame(iframe)
content = browser.find_element(By.XPATH, value = "//body").text
print(content)
=======
driver = webdriver.Chrome()

#provide website

url = "https://merolagani.com"

driver.get(url)
driver.maximize_window()
title = driver.title
print(title)
time.sleep(3)

driver.quit()
>>>>>>> 00d42342092d210e860dccbe87d780b55c20093a
