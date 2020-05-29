from selenium.webdriver.support.select import Select
from locators import locators


class AccountPageObject:

    def __init__(self, driver):
        self.driver = driver
        self.my_account = locators.AccountLocators.my_account
        self.register_email = locators.AccountLocators.register_email
        self.register_password = locators.AccountLocators.register_password
        self.register_button = locators.AccountLocators.register_button
        self.login_email = locators.AccountLocators.login_email
        self.login_password = locators.AccountLocators.login_password
        self.login_button = locators.AccountLocators.login_button
        self.account_details = locators.AccountLocators.account_details
        self.account_first_name = locators.AccountLocators.account_first_name
        self.account_last_name = locators.AccountLocators.account_last_name
        self.password_current = locators.AccountLocators.password_current
        self.new_password = locators.AccountLocators.new_password
        self.confirm_password = locators.AccountLocators.confirm_password
        self.save_changes_button = locators.AccountLocators.save_changes_button
        self.addresses_link = locators.AccountLocators.addresses_link
        self.billing_address_edit = locators.AccountLocators.billing_address_edit
        self.billing_first_name = locators.AccountLocators.billing_first_name
        self.billing_last_name = locators.AccountLocators.billing_last_name
        self.billing_country = locators.AccountLocators.billing_country
        self.billing_address = locators.AccountLocators.billing_address
        self.billing_postcode = locators.AccountLocators.billing_postcode
        self.billing_city = locators.AccountLocators.billing_city
        self.billing_phone = locators.AccountLocators.billing_phone
        self.save_address_button = locators.AccountLocators.save_address_button
        self.shipping_address_edit = locators.AccountLocators.shipping_address_edit
        self.shipping_first_name = locators.AccountLocators.shipping_first_name
        self.shipping_last_name = locators.AccountLocators.shipping_last_name
        self.shipping_country = locators.AccountLocators.shipping_country
        self.shipping_address = locators.AccountLocators.shipping_address
        self.shipping_postcode = locators.AccountLocators.shipping_postcode
        self.shipping_city = locators.AccountLocators.shipping_city
        self.shipping_phone = locators.AccountLocators.shipping_phone

    def get_my_account(self):
        self.driver.find_element(*self.my_account).click()

    #registration
    def fill_registration_data(self, email, password):
        self.driver.find_element(*self.register_email).send_keys(email)
        self.driver.find_element(*self.register_password).send_keys(password)

    def submit_registration_data(self):
        self.driver.find_element(*self.register_button).click()

    #login
    def fill_login_data(self, email, password):
        self.driver.find_element(*self.login_email).send_keys(email)
        self.driver.find_element(*self.login_password).send_keys(password)

    def submit_login_data(self):
        self.driver.find_element(*self.login_button).click()

    #change password
    def get_account_details(self):
        self.driver.find_element(*self.account_details).click()

    def clear_name_inputs(self):
        self.driver.find_element(*self.account_first_name).clear()
        self.driver.find_element(*self.account_last_name).clear()

    def fill_name_inputs(self, name, lastname):
        self.driver.find_element(*self.account_first_name).send_keys(name)
        self.driver.find_element(*self.account_last_name).send_keys(lastname)

    def fill_password_data(self, current_password, new_password):
        self.driver.find_element(*self.password_current).send_keys(current_password)
        self.driver.find_element(*self.new_password).send_keys(new_password)
        self.driver.find_element(*self.confirm_password).send_keys(new_password)

    def save_changes(self):
        self.driver.find_element(*self.save_changes_button).click()

    #billing / shipping addresses

    def get_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.billing_address_edit).click()

    def fill_billing_name(self, name, lastname):
        self.driver.find_element(*self.billing_first_name).clear() #in case test_password_change already filled the info
        self.driver.find_element(*self.billing_last_name).clear() #in case test_password_change already filled the info
        self.driver.find_element(*self.billing_first_name).send_keys(name)
        self.driver.find_element(*self.billing_last_name).send_keys(lastname)

    def fill_billing_address(self, country, billing_address, billing_postcode, billing_city, billing_phone):
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

    def save_billing_address(self):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(*self.save_address_button))
        self.driver.find_element(*self.save_address_button).click()

    def get_shipping_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.shipping_address_edit).click()

    def fill_shipping_name(self, name, lastname):
        self.driver.find_element(*self.shipping_first_name).clear() #in case test_password_change already filled the info
        self.driver.find_element(*self.shipping_last_name).clear() #in case test_password_change already filled the info
        self.driver.find_element(*self.shipping_first_name).send_keys(name)
        self.driver.find_element(*self.shipping_last_name).send_keys(lastname)

    def fill_shipping_address(self, country, shipping_address, shipping_postcode, shipping_city):
        select = Select(self.driver.find_element(*self.shipping_country))
        select.select_by_visible_text(country)
        self.driver.find_element(*self.shipping_address).clear()
        self.driver.find_element(*self.shipping_address).send_keys(shipping_address)
        self.driver.find_element(*self.shipping_postcode).clear()
        self.driver.find_element(*self.shipping_postcode).send_keys(shipping_postcode)
        self.driver.find_element(*self.shipping_city).clear()
        self.driver.find_element(*self.shipping_city).send_keys(shipping_city)

    def save_shipping_address(self):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(*self.save_address_button))
        self.driver.find_element(*self.save_address_button).click()