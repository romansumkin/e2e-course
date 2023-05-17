import time
import math
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.support.ui import WebDriverWait





@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_guest_should_see_login_link(browser, link):

    browser.implicitly_wait(15)
    browser.get(link)
    login_button = browser.find_element(By.CSS_SELECTOR, "#ember33")
    login_button.click()
    email = browser.find_element(By.CSS_SELECTOR,"[name='login']")
    email.send_keys("sumkin.romanw@gmail.com")
    password = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    password.send_keys("Ura-gK*!cX79uR)")
    submit_button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    submit_button.click()

    time.sleep(5)
    answer = str(math.log(int(time.time())))
    answer_field = browser.find_element(By.CSS_SELECTOR, ".textarea")

    answer_field.send_keys(answer)

    time.sleep(5)
    send_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    send_button.click()

    hint = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    time.sleep(5)

    assert hint.text == "Correct!", f"get: {hint.text}"


if __name__ == "__main__":
     test_guest_should_see_login_link()