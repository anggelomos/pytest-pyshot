from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    driver = None

    @classmethod
    def start_browser(cls, driver: WebDriver):
        cls.driver = driver
        cls.driver.maximize_window()

    @classmethod
    def close_browser(cls):
        cls.driver.quit()
