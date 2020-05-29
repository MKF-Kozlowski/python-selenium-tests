from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.account_page_object import AccountPageObject


class TestBillingData:

    def test_billing_data(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://seleniumdemo.com')

        a = AccountPageObject(self.driver)
        a.get_my_account()
        a.fill_login_data('fakeemail123@gmail.com', '1234haslo123')
        a.submit_login_data()

        a.get_shipping_address()
        a.fill_shipping_name('Mike', 'Koz')
        a.fill_shipping_address('Poland', 'Zmyslona 15', '00-001', 'Pcim')
        a.save_shipping_address()
        #self.driver.find_element_by_name('save_address').click()
        self.driver.quit()