import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pege_ui import Page_ui

@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    yield driver
    driver.quit()

@allure.title("Получение фильмов с вводам данных на кириллице")
@allure.story("Получение фильма по названию")
@allure.epic("Поиск")
def test_search_cyrillic(driver):
     page_ui = Page_ui(driver)
     page_ui.search_cyrillic('Девчата')

@allure.title("Получение фильмов с вводам данных на латинице")
@allure.story("Получение фильма по названию")
@allure.epic("Поиск")
def test_search_latin(driver):
     page_ui = Page_ui(driver)
     page_ui.search_latin('Star Wars')

@allure.title("Получение фильмов с использованием дефисов в название")
@allure.story("Получение фильма по названию")
@allure.epic("Поиск")
def test_search_hyphen_beginning_the_end(driver):
     page_ui = Page_ui(driver)
     page_ui.search_hyphen_beginning_the_end('-Девчата-')

@allure.title("Получение фильмов ввод данных цифрами")
@allure.story("Получение фильма по названию")
@allure.epic("Поиск")
def test_search_figure(driver):
     page_ui = Page_ui(driver)
     page_ui.search_figure('123')

@allure.title("Получение фильмов с пустым полем ввода")
@allure.story("Получение фильма по названию")
@allure.epic("Поиск")
def test_empty_field(driver):
     page_ui = Page_ui(driver)
     page_ui.empty_field('')
