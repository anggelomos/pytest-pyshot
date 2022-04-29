from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.locators.locator_decorators import get_element, get_elements


class SearchPageLocators(BasePage):

    @classmethod
    @get_element
    def search_bar(cls):
        return By.ID, "search_form_input_homepage"

    @classmethod
    @get_element
    def search_button(cls):
        return By.ID, "search_button_homepage"
