import requests
import allure

url="https://api.kinopoisk.dev/v1.4"
header = {
    "Content-Type": "application/json",
    "X-API-KEY": "EN0MBQD-MYD42FZ-GSTE16D-7STFEQ0"
}


@allure.description("Поиск фильма по названию")
@allure.title("Поисковик")
@allure.feature("UPDATE")
def test_movie_title_search():
    """Эта функция находит фильм по названию."""
    with allure.step("Найти фильм по названию."):
     title_movie = requests.get(url +
                               '/movie/search?page=1&limit=10&query='
                               '%D0%94%D0%B5%D0%B2%D1%87%D0%B0%D1%82%D0%B0',
                               headers=header)

    assert title_movie.status_code == 200


@allure.description("Поиск фильма по id")
@allure.title("Поисковик")
@allure.feature("UPDATE")
def test_movie_title_id():
    """Эта функция находит фильм по id."""
    with allure.step("Найти фильм по id."):
     title_id = requests.get(url + '/movie/44168', headers=header)

    assert title_id.status_code == 200


@allure.description("Поиск 10 топовых фильмов")
@allure.title("Поисковик")
@allure.feature("UPDATE")
def test_movie_title_top10():
    """Эта функция находит 10 топовых фильмов."""
    with allure.step("Найти 10 топовых фильмов."):
     top_10 = requests.get(url + '/movie/random?notNullFields=top10',
                          headers=header)

    assert top_10.status_code == 200


@allure.description("Поиск 1000 топовых фильмов")
@allure.title("Поисковик")
@allure.feature("UPDATE")
def test_movie_title_top1000():
    """Эта функция находит 1000 топовых фильмов."""
    with allure.step("Найти 1000 топовых фильмов."):
     top_1000 = requests.get(url + '/movie/random?notNullFields=top1000',
                            headers=header)

    assert top_1000.status_code == 400


@allure.description("Поиск фильма по названию с добавлением символов")
@allure.title("Поисковик")
@allure.feature("UPDATE")
def test_movie_title_id_symbols():
    """Эта функция находит фильмы в названиях которых добавлены символы."""
    with allure.step("Найти фильмы с добавлением символов в название."):
     id_symbols = requests.get(url + '/movie/44168...', headers=header)

    assert id_symbols.status_code == 400
