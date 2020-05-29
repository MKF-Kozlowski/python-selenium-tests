from selenium.webdriver.common.by import By


class AccountLocators:

    #for registration and login
    my_account = (By.LINK_TEXT, 'My account')
    register_email = (By.ID, 'reg_email')
    register_password = (By.ID, 'reg_password')
    register_button = (By.NAME, 'register')
    login_email = (By.ID, 'username')
    login_password = (By.ID, 'password')
    login_button = (By.NAME, 'login')
    #account details and password change
    account_details = (By.LINK_TEXT, 'Account details')
    account_first_name = (By.ID, 'account_first_name')
    account_last_name = (By.ID, 'account_last_name')
    password_current = (By.ID, 'password_current')
    new_password = (By.ID, 'password_1')
    confirm_password = (By.ID, 'password_2')
    save_changes_button = (By.NAME, 'save_account_details')
    #Addresses - billing and shipping
    addresses_link = (By.LINK_TEXT, 'Addresses')
    billing_address_edit = (By.LINK_TEXT, 'Edit')
    billing_first_name = (By.ID, 'billing_first_name')
    billing_last_name = (By.ID, 'billing_last_name')
    billing_country = (By.ID, 'billing_country')
    billing_address = (By.ID, 'billing_address_1')
    billing_postcode = (By.ID, 'billing_postcode')
    billing_city = (By.ID, 'billing_city')
    billing_phone = (By.ID, 'billing_phone')
    save_address_button = (By.XPATH, '//button[@value="Save address"]')
    shipping_address_edit = (By.XPATH, '//h3[text()="Shipping address"]/following-sibling::a')
    shipping_first_name = (By.ID, 'shipping_first_name')
    shipping_last_name = (By.ID, 'shipping_last_name')
    shipping_country = (By.ID, 'shipping_country')
    shipping_address = (By.ID, 'shipping_address_1')
    shipping_postcode = (By.ID, 'shipping_postcode')
    shipping_city = (By.ID, 'shipping_city')
    shipping_phone = (By.ID, 'shipping_phone')


class ShoppingLocators:

    shop_link = (By.XPATH, '//span[contains(text(), "Shop")]')
    bdd_cucumber_info = (By.XPATH, '//h2[contains(text(), "BDD Cucumber")]')
    quantity_input = (By.XPATH, '//div[@class="quantity"]/ input')
    add_to_cart_button = (By.NAME, 'add-to-cart')
    cart_confirmation_message = (By.CLASS_NAME, 'woocommerce-message')
    view_cart_link = (By.LINK_TEXT, 'View cart')
    checkout = (By.PARTIAL_LINK_TEXT, 'checkout')
    place_order = (By.XPATH, '//button[@value="Place order"]')
    order_confirmation_message = (By.CLASS_NAME, 'woocommerce-thankyou-order-received')
