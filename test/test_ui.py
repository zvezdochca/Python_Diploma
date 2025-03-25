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

@allure.story("Ввод значений в поле поиск")
@allure.epic("Поиск")
def test_search_cyrillic(driver):
    with allure.step("Ввод данных на кириллице."):
     page_ui = Page_ui(driver)
     page_ui.search_cyrillic('Девчата')

@allure.story("Ввод значений в поле поиск")
@allure.epic("Поиск")
def test_search_latin(driver):
    with allure.step("Ввод данных на латинице."):
     page_ui = Page_ui(driver)
     page_ui.search_latin('Star Wars')

@allure.story("Ввод значений в поле поиск")
@allure.epic("Поиск")
def test_search_hyphen_beginning_the_end(driver):
    with allure.step("Ввод данных с дефисам."):
     page_ui = Page_ui(driver)
     page_ui.search_hyphen_beginning_the_end('-Девчата-')

@allure.story("Ввод значений в поле поиск")
@allure.epic("Поиск")
def test_search_figure(driver):
    with allure.step("Ввод данных цифрами."):
     page_ui = Page_ui(driver)
     page_ui.search_figure('123')

@allure.story("Ввод значений в поле поиск")
@allure.epic("Поиск")
def test_empty_field(driver):
    with allure.step("Пустое поле ввода."):
     page_ui = Page_ui(driver)
     page_ui.empty_field('')
