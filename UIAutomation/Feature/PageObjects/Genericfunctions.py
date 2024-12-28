from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

class GenericMethods :
    def __init__(self,driver):
        self.driver = driver


    def open_url(self,url):
        self.driver.get(url)
        self.wait_till_title()

    def wait_till_title(self):
        wait=WebDriverWait(self.driver,100)
        wait.until(expected_conditions.title_contains("Currency Exchange Rates"))

    def click_element_by_xpath(self,Locator):
        self.elementClickbale(Locator)
        self.driver.find_element(By.XPATH,Locator).click()

    def send_keys(self,value,Locator):
        self.driver.find_element(By.XPATH,Locator).send_keys(value)

    def elementClickbale(self,Locator):
        wait = WebDriverWait(self.driver, 100)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locator)))
    def WaitTillElementVisible(self,Locator):
        wait = WebDriverWait(self.driver, 100)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH , Locator)))

    def return_text(self,Locator):
        self.WaitTillElementVisible(Locator)
        return self.driver.find_element(By.XPATH, Locator).text










