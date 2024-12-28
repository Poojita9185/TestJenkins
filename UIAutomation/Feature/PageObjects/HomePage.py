import time

from Feature.PageLocators import PageLoc
from Feature.PageObjects.Genericfunctions import GenericMethods

class Homepage(GenericMethods) :

    def send_data(self,value,Locator):
        self.send_keys(value, Locator)

    def select_from_dropdown(self,dropdown,currency):
        self.send_data(currency , PageLoc.enter_currency.replace('?',str(dropdown).title()) )
        self.click_element_by_xpath(PageLoc.select_currency.replace('?',currency))

    def click_button(self):
        self.click_element_by_xpath(PageLoc.convert_button_xpath)

    def retreive_text(self):
        value = self.return_text(PageLoc.overall_currency_xpath)
        print(value)
        return value













