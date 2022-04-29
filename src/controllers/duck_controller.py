from config import duck_search_page_url
from src.pages.base_page import BasePage
from src.pages.results_page import ResultsPage
from src.pages.search_page import SearchPage


class DuckController:

    @classmethod
    def open_search_page(cls):
        BasePage.driver.get(duck_search_page_url)

    @classmethod
    def search(cls, search_text: str):
        SearchPage.enter_search_text(search_text)
        SearchPage.make_search()

    @classmethod
    def search_image(cls, search_text: str):
        cls.search(search_text)
        ResultsPage.search_image()

    @classmethod
    def verify_search_result(cls, search_text: str):
        first_result = ResultsPage.get_result_list()[0]
        return search_text in first_result.text

    @classmethod
    def verify_image_search_result(cls):
        first_result = ResultsPage.get_image_result_list()[0]
        return first_result.is_displayed()
