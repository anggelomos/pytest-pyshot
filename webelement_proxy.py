from selenium.webdriver.remote.webelement import WebElement


class WebElementProxy(WebElement):

    def __init__(self, webelement: WebElement, webdriver):
        self.__dict__.update(webelement.__dict__)
        self.webdriver = webdriver

    def send_keys(self, *value):
        super().send_keys(*value)
        self.webdriver.save_screenshot()

    def click(self):
        super().click()
        self.webdriver.save_screenshot()
