from selenium.webdriver.common.by import By
from settings import valid_phone, valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl import element_has_css_class
import time
import pytest
@pytest.mark.auth_phone
def test_auth_with_phone(driver):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # проверяем что таб Телефон активен по умолчанию
   wait = WebDriverWait(driver, 10)
   element = wait.until(element_has_css_class((By.ID, 't-btn-tab-phone'), "rt-tab--active"))
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys(valid_phone)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Маркова\nАнна')
   )
   assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Маркова"
   assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Анна"
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_mail
def test_auth_with_email(driver):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на таб Почта
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим почту
   driver.find_element(By.ID, 'username').send_keys(valid_email)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Маркова\nАнна')
   )
   assert driver.find_element(By.CLASS_NAME, 'user-name__last-name').text == "Маркова"
   assert driver.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text == "Анна"
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента