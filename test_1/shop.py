
import logging
import sys
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from ui.locator import CheckOutLocators as Lc
from ui.locator import itemlocator as li
from test_1.basic_fun import verify_page_title

class InventoryPage:

    def __init__(self, driver: WebDriver, timeout: int = 10):

        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        logging.info("InventoryPage initialized")
        verify_page_title(self.driver,"Products")
        logging.info("verify title page")

    #Add the 3 first items to cart
    def select_item(self):
            added = []
            count=0
            try:
                logging.info(" Searching product cards")
                cards = self.driver.find_elements(*li.ITEM_CARD)
                logging.info(" Found  products ")
                #add the 3 product to cart
                for idx, card in enumerate(cards, start=1):
                    if count == 3:
                        logging.info("Have 3 product to cart ")
                        break
                    logging.info("Get the product name and remove extra spaces ")
                    name = card.find_element(*li.ITEM_NAME).text.strip()
                    btn = card.find_element(*li.ADD_BUTTON)
                    logging.info("Get the button text")
                    btn_text = btn.text
                    logging.info("Check the name of the button- if the name add to cart add the item to cart")
                    if btn_text.strip().lower()  == "add to cart":
                        btn.click()
                        added.append(name)
                        count += 1
                        logging.info(f" Added product #: {name}")
                        print(f" Added product #: {name}")
                    else:
                        logging.info(f"Product already in cart: {name}")
                    logging.info(f"Finished adding items: {added}")
            except Exception :
                logging.error(" Failed to add  three products.")
                sys.exit(1)
            return added

    def checkout(self):# finish the checkout process
        logging.info(" Go to the Cart and clicks to Checkout.")
        try:
            self.driver.find_element(*Lc.CART_BUTTON).click()
            self.driver.find_element(*Lc.CHECKOUT_BUTTON).click()
            logging.info(f" go to the Cart and clicks to Checkout.")
        except Exception :
            logging.error(" Failed to go to cart and clicks to Checkout.")
            sys.exit(1)

    def sort_by_name_or_price(self,sort_v):
        try:
            logging.info(" Go to the Cart and clicks to Sort by name or price.")
            dropdown = Select(self.driver.find_element(*li.SORT_DROP))
            logging.info(" preform sort")
            dropdown.select_by_value(sort_v)
        except Exception :
            logging.error(" Failed to sort by name or price.")
            sys.exit(1)
        finally:
            logging.info(" Finished preform sort.")
            print("sort product list:")
            item_names = self.driver.find_elements(*li.ITEM_NAME)
            names = [item.text.strip() for item in item_names]
            [print (i) for i in names]














