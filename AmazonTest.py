import time
import unittest
from selenium import webdriver
from Pages.MainPage import MainPageClass
from Pages.MyAccountHomePage import MyAccountHomePageClass


class AmazonSimpleTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.mainPage = MainPageClass(self.driver)
        #self.myAccountHomePage = MyAccountHomePageClass(self.driver)



    def test_simpleTC(self):
        self.driver.get("https://www.amazon.com/")
        self.mainPage.press_amazon_SignIn_account_Button()
        self.mainPage.fill_signin_field("kimkrugeractress@gmail.com")

        time.sleep(4)
        self.mainPage.press_amazon_continue_Button()

        time.sleep(3)
        self.mainPage.fill_password_field("kim2002++")

        time.sleep(5)
        self.mainPage.press_amazon_checkbox_field()

        time.sleep(5)
        self.mainPage.press_amazon_SignIn_Button()

        time.sleep(5)
        self.MyAccountHomePage.press_amazon_bucket_Button()



    def tearDown(self):
        time.sleep(4)
        self.driver.close()