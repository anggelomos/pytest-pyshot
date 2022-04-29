import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_proxy import WebDriverProxy


def pyshot_driver(screenshot_path: str):
    def inner(func):
        def wrapper(*args):
            return WebDriverProxy(func(*args), screenshot_path)
        return wrapper
    return inner


@pytest.fixture(scope="module", autouse=True)
@pyshot_driver("C:/Users/angel/OneDrive/Documentos/projects/pyshot/screenshots")
def chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     for key, value in item.funcargs.items():
#         if isinstance(value, WebDriver):
#             item.funcargs[key] = WebDriverProxy(value, "C:/Users/angel/OneDrive/Documentos/projects/pyshot/screenshots")
#
#     outcome = yield
