from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class WebElementProxy(WebElement):

    def __init__(self, webelement: WebElement, webdriver):
        self.__dict__.update(webelement.__dict__)
        self.webdriver = webdriver

    def find_element(self, by=By.ID, value=None):
        return WebElementProxy(super().find_element(by, value), self.webdriver)

    def find_elements(self, by=By.ID, value=None) -> list:
        return [WebElementProxy(element, self.webdriver) for element in super().find_elements(by, value)]

    def send_keys(self, *value):
        super().send_keys(*value)
        self.webdriver.save_screenshot()

    def click(self):
        super().click()
        self.webdriver.save_screenshot()

    def clear(self):
        super().clear()
        self.webdriver.save_screenshot()
