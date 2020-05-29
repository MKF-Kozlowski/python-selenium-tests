from selenium.webdriver.support.select import Select
from locators import locators


class ShoppingObject:

    def __init__(self, driver):
        self.driver = driver
        self.shop_link = locators.ShoppingLocators.shop_link
        self.bdd_cucumber_info = locators.ShoppingLocators.bdd_cucumber_info
        self.quantity_input = locators.ShoppingLocators.quantity_input
        self.add_to_cart_button = locators.ShoppingLocators.add_to_cart_button
        self.cart_confirmation_message = locators.ShoppingLocators.cart_confirmation_message
        self.view_cart_link = locators.ShoppingLocators.view_cart_link
        self.checkout = locators.ShoppingLocators.checkout
        self.place_order = locators.ShoppingLocators.place_order
        self.order_confirmation_message = locators.ShoppingLocators.order_confirmation_message
        self.billing_first_name = locators.AccountLocators.billing_first_name
        self.billing_last_name = locators.AccountLocators.billing_last_name
        self.billing_country = locators.AccountLocators.billing_country
        self.billing_address = locators.AccountLocators.billing_address
        self.billing_postcode = locators.AccountLocators.billing_postcode
        self.billing_city = locators.AccountLocators.billing_city
        self.billing_phone = locators.AccountLocators.billing_phone

    def go_shopping(self):
        self.driver.find_element(*self.shop_link).click()

    def bdd_cucumber_order(self):
        self.driver.find_element(*self.bdd_cucumber_info).click()
        self.driver.find_element(*self.quantity_input).clear()
        self.driver.find_element(*self.quantity_input).send_keys('2')
        self.driver.find_element(*self.add_to_cart_button).click()
        assert '“BDD Cucumber” have been added to your cart.' in self.driver.find_element(*self.cart_confirmation_message).text
        self.driver.find_element(*self.view_cart_link).click()

    def checkout(self):
        self.driver.find_element(*self.checkout).click()

    def fill_billing_data_of_order(self, name, lastname, country, billing_address, billing_postcode, billing_city, billing_phone):
        self.driver.find_element(*self.billing_first_name).clear()  # in case test_password_change already filled the info
        self.driver.find_element(*self.billing_last_name).clear()  # in case test_password_change already filled the info
        self.driver.find_element(*self.billing_first_name).send_keys(name)
        self.driver.find_element(*self.billing_last_name).send_keys(lastname)
        select = Select(self.driver.find_element(*self.billing_country))
        select.select_by_visible_text(country)
        self.driver.find_element(*self.billing_address).clear() #in case elements are already filled
        self.driver.find_element(*self.billing_address).send_keys(billing_address)
        self.driver.find_element(*self.billing_postcode).clear()
        self.driver.find_element(*self.billing_postcode).send_keys(billing_postcode)
        self.driver.find_element(*self.billing_city).clear()
        self.driver.find_element(*self.billing_city).send_keys(billing_city)
        self.driver.find_element(*self.billing_phone).clear()
        self.driver.find_element(*self.billing_phone).send_keys(billing_phone)

    def place_order(self):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(*self.place_order))
        self.driver.find_element(*self.place_order).click()

    def assert_order(self):
        assert 'Thank you. Your order has been received.' in self.driver.find_element(*self.order_confirmation_message).text


