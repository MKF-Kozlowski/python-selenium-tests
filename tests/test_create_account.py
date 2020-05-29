from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.account_page_object import AccountPageObject


class TestCreateAccount:

    def test_create_account(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://seleniumdemo.com')

        a = AccountPageObject(self.driver)
        a.get_my_account()
        a.fill_registration_data('fakeemail123@gmail.com', '1234haslo123')
        a.submit_registration_data()

        self.driver.quit()