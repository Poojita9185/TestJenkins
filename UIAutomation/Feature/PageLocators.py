class PageLoc :

    Enter_amount_feild = "//span[@class='amount-input']/input"
    enter_currency = "//div[@id = 'midmarket?Currency']//input"
    select_currency = "//div[contains(text(),'?')]"
    convert_button_xpath = "//button[text()='Convert']"
    overall_currency_xpath = "//label[text()='Amount']/parent :: div /parent :: div/following-sibling :: div//p[2]"
