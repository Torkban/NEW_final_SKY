from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import allure
from ConfigProvider import ConfigProvide


class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
       self.__url__ = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fu%252Fjoyejey913%252Fboards%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D"
       #self.__url__ = ConfigProvide().get_uis_url() + "login"
       self.__driver = driver
    
    @allure.step("Открыть страницу авторизации")
    def go(self, url = "defolt"):
        if url == "defolt":
            self.__driver.get(self.__url__)
        else:
            self.__driver.get(url)
    
    @allure.step("Авторизоваться под {email}:{password}")   
    def login_as(self, email: str, password: str):
        #Находим поле с логином. Передаем в него значение переменной email:
        self.__driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)

        #Кликаем на кнопку «Продолжить»:
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

        #Дожидаемся, когда поле «Введите пароль» отрисуется:
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role=presentation]")))
        
        #Находим поле «Введите пароль», передаем ему значение переменной password:
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

        #Находим кнопку «Войти» и нажимаем на нее
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    #Возвращаем текущий URL
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url

'''
class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
       #self.__url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fu%252Fjoyejey913%252Fboards%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D"
       self.__url__ = ConfigProvide().get_uis_url() + "login"
       self.__driver = driver
    
    @allure.step("Открыть страницу авторизации")
    def go(self):
       self.__driver.get(self.__url__)
    
    @allure.step("Авторизоваться под {email}:{password}")   
    def login_as(self, email: str, password: str):
        #Находим поле с логином. Передаем в него значение переменной email:
        self.__driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)

        #Кликаем на кнопку «Продолжить»:
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

        #Дожидаемся, когда поле «Введите пароль» отрисуется:
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role=presentation]")))
        
        #Находим поле «Введите пароль», передаем ему значение переменной password:
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

        #Находим кнопку «Войти» и нажимаем на нее
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    #Возвращаем текущий URL
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url
        
'''