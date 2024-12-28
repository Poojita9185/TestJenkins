from selenium import webdriver
from Feature.Utilities.TestData import Testdata


def get_driver():

    browser = Testdata.Browser
    if browser.upper() == "CHROME":
        driver = webdriver.Chrome()
    elif browser.upper() == "EDGE":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    return driver