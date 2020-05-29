from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.account_page_object import AccountPageObject


class TestPasswordChange:

    def test_password_change(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://seleniumdemo.com')

        a = AccountPageObject(self.driver)
        a.get_my_account()
        a.fill_login_data('fakeemail123@gmail.com', '1234haslo123')
        a.submit_login_data()
        a.get_account_details()
        a.clear_name_inputs()
        a.fill_name_inputs('Mike', 'Kozlowski')
        a.fill_password_data('1234haslo123', '1234haslo1234')
        a.save_changes()
        assert "Account details changed successfully" in self.driver.find_element_by_class_name('woocommerce-message').text

        self.driver.quit()

    def test_reset_password(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://seleniumdemo.com')

        a = AccountPageObject(self.driver)
        a.get_my_account()
        a.fill_login_data('fakeemail123@gmail.com', '1234haslo1234')
        a.submit_login_data()
        a.get_account_details()
        a.clear_name_inputs()
        a.fill_name_inputs('Mike', 'Kozlowski')
        a.fill_password_data('1234haslo1234', '1234haslo123')
        a.save_changes()
        assert "Account details changed successfully" in self.driver.find_element_by_class_name('woocommerce-message').text

        self.driver.quit()
