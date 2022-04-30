import configparser

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_proxy import WebDriverProxy


def pytest_addoption(parser):
    group = parser.getgroup("pyshot", "Facilitate screenshot taking with selenium during testcases")
    group.addoption("--pyshot_conf",
                    action="store",
                    default="pyshot.conf",
                    help="Absolute path to the file pyshot.conf, example. /usr/test/pyshot.conf")


def pyshot_driver(func):
    def wrapper(*args):
        return WebDriverProxy(func(*args))
    return wrapper


def pyshot_step(func):
    def wrapper(*args):

        if WebDriverProxy.only_pyshot_steps:
            WebDriverProxy.enable_screenshots()
            value = func(*args)
            WebDriverProxy.disable_screenshots()
        else:
            value = func(*args)

        return value
    return wrapper


@pytest.fixture(scope="module", autouse=True)
@pyshot_driver
def chrome_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def pytest_runtest_call(item):
    pyshot_conf_path = item.config.getvalue("pyshot_conf")
    default_section = "pyshot"
    parser = configparser.ConfigParser()
    parser.read(pyshot_conf_path)

    screenshots_path = parser.get(default_section, "screenshots_path", fallback="")
    only_pyshot_steps = parser.getboolean(default_section, "only_pyshot_steps", fallback=False)
    create_folder_per_testcase = parser.getboolean(default_section, "create_folder_per_testcase", fallback=True)

    if only_pyshot_steps:
        WebDriverProxy.only_pyshot_steps = True
        WebDriverProxy.disable_screenshots()

    if create_folder_per_testcase and item.name:
        screenshots_path += f"/{item.name[:220]}_{WebDriverProxy.get_timestamp()}"

    if not WebDriverProxy.screenshots_path:
        WebDriverProxy.set_screenshots_path(screenshots_path)

    for value in item.funcargs.values():
        if isinstance(value, WebDriverProxy):
            value.save_screenshot()


def pytest_runtest_teardown(item, nextitem):

    for value in item.funcargs.values():
        if isinstance(value, WebDriverProxy):
            value.save_screenshot()

    WebDriverProxy.set_screenshots_path("")
    WebDriverProxy.only_pyshot_steps = False
    WebDriverProxy.enable_screenshots()
