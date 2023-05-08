from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Ivanov")

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("ivanov@iavan.com")


    pick_file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'attach_file_l2_s8.txt')
    pick_file_button.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()