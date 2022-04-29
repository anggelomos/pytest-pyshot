import pytest
from src.controllers.duck_controller import DuckController
from src.pages.base_page import BasePage


@pytest.fixture(scope="module", autouse=True)
def setup(chrome_driver):
    BasePage.start_browser(chrome_driver)
    yield


@pytest.fixture(scope="module", autouse=True)
def teardown():
    yield
    BasePage.close_browser()


def test_search_term():
    search_term = "Apple"

    DuckController.open_search_page()
    DuckController.search(search_term)

    assert DuckController.verify_search_result(search_term)


def test_search_image():
    search_term = "Python"

    DuckController.open_search_page()
    DuckController.search_image(search_term)

    assert DuckController.verify_image_search_result()
