import os
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webelement_proxy import WebElementProxy


class WebDriverProxy(WebDriver):

    screenshots_path = ""

    def __init__(self, webdriver: WebDriver, screenshots_path: str = ""):
        self.__dict__.update(webdriver.__dict__)

        if not self.screenshots_path:
            self.set_screenshots_path(screenshots_path)

    def set_screenshots_path(self, path: str) -> None:
        self.screenshots_path = path

        if not os.path.exists(path):
            os.makedirs(path)

    def save_screenshot(self, filename="") -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
        super().save_screenshot(f"{self.screenshots_path}/{timestamp}.png")

    def get(self, url: str) -> None:
        super().get(url)
        self.save_screenshot()

    def find_element(self, by=By.ID, value=None) -> WebElementProxy:
        return WebElementProxy(super().find_element(by, value), self)

    def find_elements(self, by=By.ID, value=None) -> list:
        return [WebElementProxy(element, self) for element in super().find_elements(by, value)]

    def quit(self) -> None:
        self.save_screenshot()
        super().quit()
