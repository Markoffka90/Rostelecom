from selenium.webdriver.common.by import By
from settings import valid_phone, valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl import element_has_css_class
import time
import pytest
@pytest.mark.auth_phone
@pytest.mark.parametrize("phone", ['1', '+7910374995'], ids=['one digit', 'invalid format'])
def test_auth_phone_invalid_format(driver, phone):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys(phone)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Проверяем текст ошибки
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.CLASS_NAME, 'rt-input-container__meta--error'), 'Неверный формат телефона')
   )
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента

@pytest.mark.auth_phone
@pytest.mark.parametrize("phone", ['', '          '], ids=['empty', 'only blanks'])
def test_auth_phone_empty_phone(driver, phone):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys(phone)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.ID, 'rt-input-container__meta--error'), 'Введите номер телефона')
   )
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_phone
@pytest.mark.parametrize("phone", ['0000000000', '555555555555'], ids= ['wrong phone', 'invalid phone 11 number'])
def test_auth_phone_wrong_user_name(driver, phone):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys(phone)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_phone
@pytest.mark.xfail
@pytest.mark.parametrize("passw", ['', '          '], ids= ['empty', 'only blanks'])
def test_auth_phone_empty_pass(driver, passw):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys(valid_phone)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(passw)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.ID, 'rt-input-container__meta--error'), 'Введите пароль')
   )
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_phone
@pytest.mark.parametrize("passw", ['66666666666', 'djfhdjfhdlkfj'], ids= ['wrong passord number', 'invalid password letters'])
def test_auth_phone_wrong_pass(driver, passw):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Вводим телефон
   driver.find_element(By.ID, 'username').send_keys(valid_phone)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(passw)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_mail
@pytest.mark.parametrize("mail", ['dsjhdg@fg.ru', 'jhjdf@df.com'], ids= ['wrong mail', 'invalid mail'])
def test_auth_mail_wrong_user_name(driver, mail):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим почту
   driver.find_element(By.ID, 'username').send_keys(mail)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_mail
@pytest.mark.parametrize("mail", ['', '          '], ids= ['empty', 'only blanks'])
def test_auth_mail_empty_mail(driver, mail):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим адрес
   driver.find_element(By.ID, 'username').send_keys(mail)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.ID, 'rt-input-container__meta--error'), 'Введите адрес, указанный при регистрации')
   )
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_mail
@pytest.mark.xfail
def test_auth_mail_invalid_format(driver):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим почту
   driver.find_element(By.ID, 'username').send_keys('annet44_91@@mail.ru')
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Проверяем текст ошибки
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.CLASS_NAME, 'rt-input-container__meta--error'), 'Неверный формат почты')
   )
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
@pytest.mark.auth_mail
@pytest.mark.parametrize("passw", ['66666666666', 'jhgjkhkjlkjk'], ids= ['wrong passord number', 'invalid password letters'])
def test_auth_mail_wrong_pass(driver, passw):
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   driver.find_element(By.ID, 't-btn-tab-mail').click()
   # проверяем что таб Почта активен
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 't-btn-tab-mail'), "rt-tab--active"))
   # Вводим почту
   driver.find_element(By.ID, 'username').send_keys(valid_email)
   # Вводим пароль
   driver.find_element(By.ID, 'password').send_keys(passw)
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Ждем когда окажемся на главной странице пользователя
   WebDriverWait(driver, 11).until(
      EC.text_to_be_present_in_element((By.ID, 'form-error-message'), 'Неверный логин или пароль')
   )
   # проверяем ссылка Забыл пароль оранжевая
   wait = WebDriverWait(driver, 10)
   wait.until(element_has_css_class((By.ID, 'forgot_password'), "rt-link--orange"))
   time.sleep(5)  # небольшая задержка, чисто ради эксперимента