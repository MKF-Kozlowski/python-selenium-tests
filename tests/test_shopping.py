import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.account_page_object import AccountPageObject
from page_objects.shopping_object import ShoppingObject


class TestBillingData:

    def test_billing_data(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://seleniumdemo.com')

        a = AccountPageObject(self.driver)
        a.get_my_account()
        a.fill_login_data('fakeemail123@gmail.com', '1234haslo123')
        a.submit_login_data()

        s = ShoppingObject(self.driver)
        s.go_shopping()
        s.bdd_cucumber_order()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text('checkout').click()
        s.fill_billing_data_of_order('Mike', 'Koz', 'Poland', 'Zmyslona 15', '00-001', 'Pcim', '000-000-000')
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@value="Place order"]').click()
        self.driver.quit()