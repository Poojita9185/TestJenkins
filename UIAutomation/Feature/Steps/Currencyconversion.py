import time

from behave import given,when,then

from Feature.PageLocators import PageLoc
from Feature.PageObjects.HomePage import Homepage
from Feature.Utilities.Driverinitialization import get_driver
from Feature.Utilities.TestData import Testdata


@given("the User launch the url in browser")
def launch_url(context) :
    context.Homepage_obj = Homepage(context.driver)
    context.Homepage_obj.open_url(Testdata.URL)

@when("the user enters the Amount")
def click_amount(context):
    context.Homepage_obj.send_data(Testdata.amount , PageLoc.Enter_amount_feild)

@when("the user selects the Currency in '{dropdown}' field")
def select_currency(context,dropdown):
    if str(dropdown).lower() == 'from' :
        context.Homepage_obj.select_from_dropdown(dropdown,Testdata.From_Currency )
    elif str(dropdown).lower() == 'to' :
        context.Homepage_obj.select_from_dropdown(dropdown, Testdata.To_Currency )

@when("click on Convert button")
def click_convert_button(context):
    context.Homepage_obj.click_button()

@then("the converted value should be read and display")
def display_value(context):
    calculated_currency = context.Homepage_obj.retreive_text()
    time.sleep(5)












