# Rostelecom
Работа с ресурсом https://b2c.passport.rt.ru/
test_selenium_page_elements.py - проверка наличия элементов на странице согласно спецификации
test_selenium_auth.py позитивные тесты авторизации по номеру телефона и почте
test_selenium_auth_negative.py негативные тесты авторизации по номеру телефона и почте

# Настройка проекта:
1. Создаем виртуапльное окружение командой:
    python -m venv venv
2. Активируем виртуальное окружение командой (MacOS/Linux):
    source venv/bin/activate
   для Windows другая команда:
    \env\Scripts\activate.bat
3. Установка зависимостей:
    pip install -r requirements.txt
4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее виртуальное окружение
5. В папке driver содержится драйвер для работы с браузером Chome 116 версии. Рекомендуется проверить соответствие версии браузера, при необходимости обновить драйвер

# Запуск тестов:
1. Набираем в терминале команду:
    pytest -v
