from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_proxy import WebDriverProxy

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = WebDriverProxy(driver)

driver.maximize_window()
driver.get("https://duckduckgo.com/")

search_bar = driver.find_element(By.ID, "search_form_input_homepage")
search_button = driver.find_element(By.ID, "search_button_homepage")

search_bar.send_keys("Apple")
search_button.click()
