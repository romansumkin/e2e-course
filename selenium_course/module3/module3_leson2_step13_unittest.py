from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase):
    def test_positive_reg(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        email.send_keys("11111")
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .first")
        phone.send_keys("Ivanov")
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .second")
        address.send_keys("Ivanov")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual( "Congratulations! You have successfully registered!", welcome_text)

    def test_negative_reg(self):
        link = " http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        email.send_keys("11111")
        phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first_class .first")
        phone.send_keys("Ivanov")
        address = browser.find_element(By.CSS_SELECTOR, ".second_block .second_class .second")
        address.send_keys("Ivanov")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()