import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webelement_proxy import WebElementProxy


class WebDriverProxy(WebDriver):

    def __init__(self, webdriver: WebDriver):
        self.__dict__.update(webdriver.__dict__)

    def get(self, url: str) -> None:
        print("Opening a page!")
        super().get(url)
        self.save_screenshot()

    def save_screenshot(self, filename="") -> None:
        print("Saving a screenshot!")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
        super().save_screenshot(f"C:/Users/angel/OneDrive/Documentos/projects/pyshot/{timestamp}.png")

    def find_element(self, by=By.ID, value=None) -> WebElementProxy:
        print("Finding an element!")
        return WebElementProxy(super().find_element(by, value), self)

    def quit(self) -> None:
        print("Closing the browser!")
        self.save_screenshot()
        super().quit()
