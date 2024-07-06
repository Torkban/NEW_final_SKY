import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager 
from boardApi import BoardApi
from ConfigProvider import ConfigProvide
from DataProvider import DataProvide


token = DataProvide().get_token()
api = ConfigProvide().get_apis_url()
token = DataProvide().get_token()


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser_name = 'chrome'
        if browser_name == 'chrome':
           browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser_name == 'firefox':
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
    yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()
        
@pytest.fixture
def api_client() -> BoardApi:
    
    return BoardApi(api, token)

@pytest.fixture
def api_client_without_auth() -> BoardApi:
    return BoardApi("https://api/trello/com/1")

@pytest.fixture
def temporarys_board_id() -> str:
    api = BoardApi("https://api/trello/com/1", token)
    with allure.step("Предварительно создаём доску"):
        resp = api.create_board("Temporary board").get("id")
    return resp

@pytest.fixture
def delete_board() -> str:
    dictionary = {"boards_id_for_delete": ""}
    yield dictionary
    with allure.step("Удаляем доску после теста"):    
        api = BoardApi("https://api/trello/com/1", token).delete_board_by_id(dictionary.get("boards_id_for_delete"))
        
@pytest.fixture
def test_data():
    return DataProvide()

'''
@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser_name = ConfigProvide().get_choosen_browser()
        if browser_name == 'chrome':
           browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser_name == 'firefox':
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        browser.implicitly_wait(ConfigProvide().get_timeout())
        browser.maximize_window()
    yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()
        
@pytest.fixture
def api_client() -> BoardApi:
    
    return BoardApi(ConfigProvide().get_apis_url(), DataProvide().get_token())

@pytest.fixture
def api_client_without_auth() -> BoardApi:
    return BoardApi(ConfigProvide().get_apis_url())

@pytest.fixture
def temporarys_board_id() -> str:
    api = BoardApi(ConfigProvide().get_apis_url(),DataProvide().get_token())
    with allure.step("Предварительно создаём доску"):
        resp = api.create_board("Temporary board").get("id")
    return resp

@pytest.fixture
def delete_board() -> str:
    dictionary = {"boards_id_for_delete": ""}
    yield dictionary
    with allure.step("Удаляем доску после теста"):    
        api = BoardApi(ConfigProvide().get_apis_url(),DataProvide().get_token()).delete_board_by_id(dictionary.get("boards_id_for_delete"))
        
@pytest.fixture
def test_data():
    return DataProvide()
'''