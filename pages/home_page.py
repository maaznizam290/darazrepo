from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    search_field = (By.NAME, "q")
    search_button = (By.XPATH, "//div //div //a[@class='search-box__button--1oH7']")

    # Actions
    def open_website(self):
        self.driver.get("https://www.daraz.pk")

    def search_product(self, product_name):
        self.driver.find_element(*self.search_field).click()
        self.driver.find_element(*self.search_field).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()