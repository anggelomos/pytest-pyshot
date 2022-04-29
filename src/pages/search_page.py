from src.pages.base_page import BasePage
from src.pages.locators.search_page_locators import SearchPageLocators


class SearchPage(BasePage):

    @classmethod
    def enter_search_text(cls, search_text: str):
        SearchPageLocators.search_bar().send_keys(search_text)

    @classmethod
    def clean_search_bar(cls):
        SearchPageLocators.search_bar().clean()

    @classmethod
    def make_search(cls):
        SearchPageLocators.search_button().click()
