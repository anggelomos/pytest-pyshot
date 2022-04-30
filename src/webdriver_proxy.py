import os
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from webelement_proxy import WebElementProxy


class WebDriverProxy(WebDriver):

    screenshots_path = ""
    __screenshots_enabled = True
    only_pyshot_steps = False

    def __init__(self, webdriver: WebDriver):
        self.__dict__.update(webdriver.__dict__)

    @classmethod
    def get_timestamp(cls) -> str:
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")

    @classmethod
    def enable_screenshots(cls):
        cls.__screenshots_enabled = True

    @classmethod
    def disable_screenshots(cls):
        cls.__screenshots_enabled = False

    @classmethod
    def set_screenshots_path(cls, path: str) -> None:
        cls.screenshots_path = path

        if not os.path.exists(path) and path:
            os.makedirs(path)

    def save_screenshot(self, filename="") -> None:
        if self.__screenshots_enabled:
            super().save_screenshot(f"{self.screenshots_path}/{self.get_timestamp()}.png")

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
