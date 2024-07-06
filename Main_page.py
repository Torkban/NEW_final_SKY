from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import allure
from ConfigProvider import ConfigProvide
from time import sleep

class Main:
    def __init__(self, driver: WebDriver) -> None:
       self.__url__ = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fu%252Fjoyejey913%252Fboards%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D"
       #self.__url__ = ConfigProvide().get_uis_url() + "login"
       self.__driver = driver
    @allure.step("Создать доску")   
    def create_board(self, board_name = "тестовая доска"):
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='header-create-menu-button']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='header-create-board-button']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='create-board-title-input']").send_keys(board_name)
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='create-board-submit-button']").click()
        
    @allure.step("Удалить доску")    
    def delete_board(self, board_name = "тестовая доска"):
        self.__driver.find_element(By.CSS_SELECTOR, "[title ='" + board_name + "']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "[aria-label='Меню']").click()
        sleep(2)
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".board-menu-navigation-item-link-v2")))
        self.__driver.find_elements(By.CSS_SELECTOR, ".board-menu-navigation-item-link-v2")[13].click()
        self.__driver.find_element(By.CSS_SELECTOR, "[value='Закрыть']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='close-board-delete-board-button']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "[data-testid='close-board-delete-board-confirm-button']").click()
        