
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from ui.locator import CheckOutLocators
from test_1.basic_fun import *

class Checkoutclass:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        verify_page_title(self.driver,"Checkout: Overview")

    def verify_item(self,item):
        try:
            items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            check_item= [item.text for item in items]
            if sorted(item) == sorted(check_item):
                print(" All items match between cart and checkout.")
                logging.info("All items match between cart and checkout.")
            else:
                print("Fail :the items not macht")
        except Exception as e:
            logging.exception("Fail :the items not macht")
            sys.exit(1)


    def click_finish_button(self):
        try:
            logging.info(" Clicking the login button")
            button = self.driver.find_element(*CheckOutLocators.Finish_BUTTON)
            button.click()
        except Exception as e:
            print(" Failed to click finish button.")
            logging.exception("FAIL: Could not click finish button.")
            sys.exit(1)
        else:
            print(" finish button clicked successfully.")
            logging.info("PASS: finish button clicked successfully.")
            verify_page_title(self.driver,"Checkout: Complete!")
