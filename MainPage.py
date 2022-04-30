import time
from selenium.webdriver.common.by import By
from Locators.LocatorFiles import *

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver

    #def scroll_up(self):
    #    time.sleep(4)
    #    self.driver.execute_script("window.scrollto(0, 0)")

    def press_amazon_SignIn_account_Button(self):
        amazonSignInAccountButton = self.driver.find_element(*MainPageamazonSignInAccountButton)
        amazonSignInAccountButton.click()

    def fill_signin_field(self, text):
        signinfield = self.driver.find_element(*MainPagefillsigninfield)
        signinfield.send_keys(text)

    def press_amazon_continue_Button(self):
        amazonContinueButton = self.driver.find_element(*MainPagepressamazoncontinueButton)
        amazonContinueButton.click()

    def fill_password_field(self, text):
        passwordfield = self.driver.find_element(*MainPagefillpasswordfield)
        passwordfield.send_keys(text)

    def press_amazon_checkbox_field(self):
        amazoncheckboxButton = self.driver.find_element(*MainPagepressamazoncheckboxfield)
        amazoncheckboxButton.click()

    def press_amazon_SignIn_Button(self):
        amazonSignInButton = self.driver.find_element(*MainPagepressamazonSignInButton)
        amazonSignInButton.click()
