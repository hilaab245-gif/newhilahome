import logging
import sys
from logging import exception
from ui.locator import UserData, userorder

from selenium.common import TimeoutException

from ui.locator import itemlocator as li
def verify_page_title(driver, expected_title):
   try:
    header = driver.find_element(*li.TITLE)
    logging.info(f"check if the user move to next page ")
    if header.text == expected_title:
        print("the user move to ", header.text, "page")
        logging.info("PASS: User move  to next  page successfully.")
   except exception:
        logging.error("%s page did not load within the expected time.",expected_title)
        print(" Products page cannot loaded ")
        sys.exit(1)


def error_mes(driver):
    try:
        error_container = driver.find_element(*UserData.ERROR_MESSAGE)
        error_text = error_container.text
        print(f" Error mes: {error_text}")
        logging.warning(f" Login failed : {error_text}")
        driver.quit()
        sys.exit(1)
    except Exception as e:
        logging.info("Not display error message.")