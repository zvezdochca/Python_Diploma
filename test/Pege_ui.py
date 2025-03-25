import allure
from selenium.webdriver.common.by import By

@allure.severity("blocker")

class Page_ui:
    """ Этот класс представляет сущность "Поиск фильмов"."""
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.implicitly_wait(6)
        self._driver.maximize_window()

    def search_cyrillic(self, term:str) -> str:
        """Эта функция находит фильм с вводом данных на кириллице."""
        self._driver.implicitly_wait(20)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='kp_query']").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, "button[aria-label='Найти']").click()

    def search_latin(self, term:str) -> str:
        """Эта функция находит фильм с вводом данных на латинице."""
        self._driver.implicitly_wait(20)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='kp_query']").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, "button[aria-label='Найти']").click()


    def search_hyphen_beginning_the_end(self, term:str) -> str:
        """Эта функция находит фильм с вводом данных с дефисами."""
        self._driver.implicitly_wait(20)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='kp_query']").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, "button[aria-label='Найти']").click()


    def search_figure(self, term:str) -> str:
        """Эта функция находит фильм с вводом данных только цифры."""
        self._driver.implicitly_wait(20)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='kp_query']").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, "button[aria-label='Найти']").click()

    def empty_field(self, term:str) -> str:
        """Эта функция находит фильм с пустым полем ввода."""
        self._driver.implicitly_wait(20)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='kp_query']").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, "button[aria-label='Найти']").click()
