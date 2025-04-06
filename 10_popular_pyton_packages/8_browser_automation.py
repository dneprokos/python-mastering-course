# python .\10_popular_pyton_packages\8_browser_automation.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")

# This was created just for example. WebDriver project can be found here: https://github.com/dneprokos/python-webdriver
