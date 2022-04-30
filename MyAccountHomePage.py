import time
from Locators.LocatorFiles import *
from selenium.webdriver.common.by import By

class MyAccountHomePageClass():
    def __init__(self, driver):
        self.driver = driver

    def press_amazon_bucket_Button(self):
        time.sleep(2)
        bucketButton = self.driver.find_element(*MyAccountHomePagepressamazonbucketButton)
        bucketButton.click()

