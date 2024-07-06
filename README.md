# final_sky_project

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы длч работв с API
- ./db - хелперы для работы с БД
- test_config.ini - настройки тестов
- ConfigProvider - провайдер настроек
    - test_config.ini - настройки тестов
- DataProvider - провайдер тестовых данных
    - test_data.json - 

### Шаги
1. Склонировать проект 'git clone https://github.com/Torkban/final_sky_project.git'
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчЁт 'allure serve allure-files'



### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests