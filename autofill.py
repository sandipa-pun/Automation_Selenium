from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import random
import string

url = 'https://www.mindrisers.com.np/contact-us'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()
time.sleep(2)  # Allow time for page to load
driver.execute_script("window.scrollBy(0,600);")



name_field = driver.find_element(By.XPATH,"//input[@placeholder='Name']")
email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
phone_field = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")
subject_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
queries_field = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))

def generate_name():
    return '' .join(random.choices(string.ascii_letters, k=8))

def generate_email():
    domain = "abc.com"
    email_len = 5
    random_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_len))
    email = random_str + "@" + domain
    return email

def generate_phone():
    return "+977-98" + '' .join(random.choices(string.digits, k=8))

def generate_sub():
    return '' .join(random.choices(string.ascii_letters, k=50))

def generate_queries():
    return '' .join(random.choices(string.ascii_letters, k=100))


name = generate_name()
name_field.send_keys(name)
time.sleep(2)

email = generate_email()
email_field.send_keys(email)
time.sleep(2)

phone = generate_phone()
phone_field.clear()
phone_field.send_keys(phone)
time.sleep(2)

subject = generate_sub()
subject_field.send_keys(subject)
time.sleep(2)

queries = generate_queries()
queries_field.send_keys(queries)
time.sleep(2)


driver.quit()
