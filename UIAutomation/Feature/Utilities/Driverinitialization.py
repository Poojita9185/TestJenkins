import logging

from selenium import webdriver

from Utilities.TestData import Testdata


def get_driver():
    logging.basicConfig(
        level=logging.INFO,  # Set the log level to INFO or DEBUG
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logging.getLogger().addHandler(console_handler)
    logging.info("Logging is configured.")
    browser = Testdata.Browser
    if browser.upper() == "CHROME":
        driver = webdriver.Chrome()
    elif browser.upper() == "EDGE":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    return driver