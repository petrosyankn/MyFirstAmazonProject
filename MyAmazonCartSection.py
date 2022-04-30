from selenium.webdriver.common.by import By
import time

class MyAmazonCartSectionClass()
    def __init__(self, driver):
        self.driver = driver

    def delete_one_product(self):
        deleteButton = self.driver.finde_element(*cartPageDeleteButton)
        deleteButton.click()

    def delete_all_products(self):
        cartCount = self.driver.finde_element(*cartPageCartCount)
        numberOfProductsInCart = int(cartCount.text)
        while numberOfProductsInCart > 0:
            deleteButton = self.driver.finde_element(*cartPageDeleteButton)
            deleteButton.click()
            numberOfProductsInCart = -1
            time.sleep(2)









