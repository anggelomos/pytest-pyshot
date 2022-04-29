from src.pages.base_page import BasePage
from src.pages.locators.results_page_locators import ResultsPageLocators


class ResultsPage(BasePage):

    @classmethod
    def get_result_list(cls):
        return ResultsPageLocators.results_list()

    @classmethod
    def get_image_result_list(cls):
        return ResultsPageLocators.image_results_list()

    @classmethod
    def open_result_with_index(cls, index: int):
        ResultsPageLocators.results_list()[index].click()

    @classmethod
    def search_image(cls, search_text: str = ""):
        if search_text:
            ResultsPageLocators.search_bar().send_keys(search_text)
            ResultsPageLocators.search_button().click()

        ResultsPageLocators.images_tab().click()
