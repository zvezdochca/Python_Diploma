import pytest
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


def test_search_cyrillic(driver):
    page_ui = Page_ui(driver)
    page_ui.search_cyrillic('Девчата')

def test_search_latin(driver):
    page_ui = Page_ui(driver)
    page_ui.search_latin('Star Wars')

def test_search_hyphen_beginning_the_end(driver):
    page_ui = Page_ui(driver)
    page_ui.search_hyphen_beginning_the_end('-Девчата-')

def test_search_figure(driver):
    page_ui = Page_ui(driver)
    page_ui.search_figure('123')

def test_empty_field(driver):
    page_ui = Page_ui(driver)
    page_ui.empty_field('')