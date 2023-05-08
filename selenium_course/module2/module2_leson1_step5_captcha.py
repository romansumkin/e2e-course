from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    checkbox_element =  browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_element.click()

    radiobutton_element = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton_element.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()