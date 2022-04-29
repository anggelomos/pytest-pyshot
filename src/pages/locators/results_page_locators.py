import time

from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.locators.locator_decorators import get_element, get_elements


class ResultsPageLocators(BasePage):

    @classmethod
    @get_element
    def search_bar(cls):
        return By.ID, "search_form_input"

    @classmethod
    @get_element
    def search_button(cls):
        return By.ID, "search_button"

    @classmethod
    @get_elements
    def results_list(cls):
        return By.CSS_SELECTOR, "a[data-testid*='result-title-a']"

    @classmethod
    @get_element
    def images_tab(cls):
        return By.CSS_SELECTOR, "a[data-zci-link*='images']"

    @classmethod
    @get_elements
    def image_results_list(cls):
        time.sleep(2)
        return By.XPATH, "//img[contains(@class, 'tile--img__img')]"
