
import pytest
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from Auth import AuthPage
from Main_page import Main
from board_page import BoardPage
import conftest
import allure
from DataProvider import DataProvide
from time import sleep



@allure.step("Тест на добавление доски")
def est_create_desk(browser, test_data: dict):
    d_name = 'не первая тестовая доска'
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("joyejey913@fresec.com", "cmk468JKHF8.")
    m_page = Main(browser)
    browser.find_element(By.CSS_SELECTOR, ".boards-page-board-section-list-item")
    auth_page.go("https://trello.com/w/user2977deea2b3efe9b7d997256833ce350/home")
    len_before = len(browser.find_elements(By.CSS_SELECTOR, ".boards-page-board-section-list")[0].find_elements(By.CSS_SELECTOR, ".boards-page-board-section-list-item"))
    m_page.create_board(d_name)
    auth_page.go("https://trello.com/w/user2977deea2b3efe9b7d997256833ce350/home")
    len_after = len(browser.find_elements(By.CSS_SELECTOR, ".boards-page-board-section-list")[0].find_elements(By.CSS_SELECTOR, ".boards-page-board-section-list-item"))
    with allure.step("Проверить наличие доски"):
        auth_page.go("https://trello.com/")
        assert len(browser.find_elements(By.CSS_SELECTOR, "[title ='" + d_name + "']")) and len_after - len_before == 1
    m_page.delete_board(d_name)
    
        
@allure.step("Тест на удаление доски")
def est_delete_desk(browser, test_data: dict):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as("joyejey913@fresec.com", "cmk468JKHF8.")
    m_page = Main(browser)
    m_page.create_board("не тестовая доска")
    auth_page.go()
    len_before = len(browser.find_elements(By.CSS_SELECTOR, ".boards-page-board-section-list-item"))
    m_page.delete_board('не тестовая доска')
    len_after = len(browser.find_elements(By.CSS_SELECTOR, ".boards-page-board-section-list-item"))
    with allure.step("Проверить уменьшение числа досок"):
        assert len_before - len_after == 1
        

@allure.step("Тест на добавление карточки")
def test_create_card(browser, test_data: dict):
    auth_page = AuthPage(browser)
    auth_page.go()
    b_page = BoardPage(browser)
    auth_page.login_as("joyejey913@fresec.com", "cmk468JKHF8.")
    m_page = Main(browser)
    m_page.create_board("вторая не тестовая доска")
    b_page.create_column('Первая колонка')
    len_before = len(browser.find_elements(By.XPATH, "//label[contains(text(), 'Тестовая карточка')]"))
    #b_page.create_card('Тестовая карточка')
    len_after = len(browser.find_elements(By.XPATH, "//a[contains(text(), 'Тестовая карточка')]"))
    print(len_before, len_after)
    
def test_st():
    datap = DataProvide()
    print(datap.get_token())
    #DataProvide.get_token assert "ATTAa21d7958ef6564c8b72eed9ffa63068a598e4d3ad75601dd25a99793653f16ec2DA3E8A5"

    
    
"""    
__url = "https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3FreturnUrl%3D%252Fu%252Fjoyejey913%252Fboards%26display%3D%26aaOnboarding%3D%26updateEmail%3D%26traceId%3D%26ssoVerified%3D%26createMember%3D"
__driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
__driver.get(__url)
       #Находим поле с логином. Передаем в него значение переменной email:
__driver.find_element(By.CSS_SELECTOR, "#user").send_keys('email')
time.sleep(5)
"""
