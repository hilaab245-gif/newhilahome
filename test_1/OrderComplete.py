import logging
import sys

import self
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locator import userorder as LO

class OrderCompleteclass:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def userdataorder(self,username,lastname,zipcode):
        try:
            logging.info(" Waiting for FIRST_NAME field to appear")
            self.wait.until(EC.presence_of_element_located(LO.FIRST_NAME))
            logging.info(" FIRST_NAME field is visible")
            self.driver.find_element(*LO.FIRST_NAME).send_keys(username)
            logging.info(f"Entered first name: {username}")
            self.driver.find_element(*LO.LAST_NAME).send_keys(lastname)
            logging.info(f"Entered last name: {lastname}")
            self.driver.find_element(*LO.ZIP_CODE).send_keys(zipcode)
            logging.info(f" Entered ZIP code: {zipcode}")
            print(f"user data: {username}, {lastname}, {zipcode}")
        except Exception as e:
            logging.error(" Unexpected error while entering user data")
            sys.exit(1)
    def clickonbutcontion(self):
        try:
            logging.info(" Attempting to click CONTINUE button...")
            self.driver.find_element(*LO.CONTINUE_BUTTON).click()
            logging.info(" CONTINUE button clicked successfully")
        except Exception as e:
            logging.error(" Failed to click CONTINUE button")
            sys.exit(1)
    def verify_order_complete(self):
      try:
        current_url = self.driver.current_url
        print(current_url)
        logging.info(f"Current url: {current_url}")
        if "https://www.saucedemo.com/checkout-step-two.html" in current_url:
              logging.info(" Order completed successfully — on the correct page")
              print(" Order completed successfully — on the correct page")
      except Exception as e:
         logging.error(" Unexpected error during order confirmation check")








