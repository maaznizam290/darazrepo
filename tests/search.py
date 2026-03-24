from utils.driver_factory import get_driver
from pages.home_page import HomePage
import time

def test_search_product():
    driver = get_driver()

    home = HomePage(driver)

    # Step 1: Navigate
    home.open_website()

    # Step 2 & 3: Search product
    home.search_product("Iphone 14")

    time.sleep(25)
    driver.quit()