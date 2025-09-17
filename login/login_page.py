
import logging
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from ui.locator import UserData as loc
from test_1.basic_fun import *
class LoginPage:
    #
    def __init__(self,driver=None): #open browser
        logging.info("Initializing incognito Page")
        opts = Options()
        logging.debug("Chrome Options object created.")
        opts.add_argument("--incognito")
        opts.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })
        logging.debug("Password manager disabled in browser preferences.")
        try:
             logging.info("Attempting to open Chrome browser")
             self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
             logging.info("PASS: Chrome browser successfully")
        except Exception as e: #If any error occurs during browser setup- Logs a fail message
            logging.exception("FAIL: not successfully to open Chrome browser")
            sys.exit(1)

    #navigates to url
    def open_url(self, base_url: str):#open url
        logging.info("Attempting to navigate to URL: %s", base_url)  # Log the attempt to open the URL
        try:
            self.driver.get(base_url)
            print(f" Successfully opened URL: {base_url}")
            logging.info("PASS: opened %s", base_url) # Logs a success to open the url
        except Exception as e:
            print(f"If any error occurs during open the url - Logs a fail message",base_url)
            logging.exception("FAIL: could not open URL: %s", base_url)
            sys.exit(1) #Exit code 1

    def login(self,username:str,password:str):
             try:
                 logging.info("Wait until the username field is present")
                 WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.USER_NAME)
                 )
                 logging.info(" Username field detected.")
                 logging.debug("Finding locator and inserting parameters ")
                 username_field = self.driver.find_element(*loc.USER_NAME)
                 password_field = self.driver.find_element(*loc.PASSWORD)
                 logging.info(f" Entering username: {username}")
                 username_field.clear()
                 username_field.send_keys(username)
                 logging.info(" Entering password.")
                 password_field.clear()
                 password_field.send_keys(password)
             except Exception :
                 print(f" User not successful to insert user {username} and password {password}")
                 logging.exception("FAIL: User not successful to insert user: %s", username)
                 sys.exit(1)
             else:
                 print(f" User successful to insert {username} and password {password}")
                 logging.info("PASS: User successful to insert details for user: %s", username)
    def click_login_button(self):
        try:
          logging.info(" Clicking the login button")
          login_button = self.driver.find_element(*loc.LOGIN_BUTTON)
          login_button.click()
        except Exception as e:
            print(" Failed to click login button.")
            logging.exception("FAIL: Could not click login button.")
            sys.exit(1)
        else:
            print("Login button clicked successfully.")
            logging.info("PASS: Login button clicked.")
            error_mes(self.driver)










