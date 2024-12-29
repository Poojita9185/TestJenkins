from Utilities.Driverinitialization import get_driver


def before_all(context):
    context.driver = get_driver()