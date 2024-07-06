from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import allure
from ConfigProvider import ConfigProvide
from time import sleep


class BoardPage:
    def __init__(self, driver: WebDriver) -> None:
       self.__url__ = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fu%252Fjoyejey913%252Fboards%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D"
       self.__driver = driver
    
    @allure.step("Создать колонку")   
    def create_column(self, column_name = 'тестовая колонка'):
        sleep(1)
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='list-composer-button']").click()
        '''не проходит в этом месте'''
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR, "[data-testid='list-name-textarea']"))
        sleep(1)
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='list-name-textarea']").send_keys(column_name)
        print(3)
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='list-composer-add-list-button']").click()
        
        
    @allure.step("Создать карточку")   
    def create_card(self, card_name = 'тестовая карточка'):
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='list-add-card-button']").click()
        #self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='list-card-composer-textarea']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='list-card-composer-textarea']").send_keys(card_name)
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='list-card-composer-add-card-button']").click()
       