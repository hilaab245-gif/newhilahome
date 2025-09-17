from selenium.webdriver.common.by import By

class UserData:
    USER_NAME = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.ID,'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

class CheckOutLocators:
    CART_BUTTON=(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CHECKOUT_BUTTON =(By.XPATH, '//*[@id="checkout"]')
    Finish_BUTTON=(By.XPATH, '//*[@id="finish"]')


class itemlocator:
    ITEM_CARD = (By.CSS_SELECTOR, ".inventory_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ADD_BUTTON = (By.CSS_SELECTOR, ".pricebar button")
    TITLE=(By.CSS_SELECTOR, '[data-test="title"]')
    SORT_DROP=(By.CSS_SELECTOR, '[data-test="product-sort-container"]')


class userorder:
     FIRST_NAME=(By.ID, 'first-name')
     LAST_NAME=(By.ID, 'last-name')
     ZIP_CODE=(By.ID, 'postal-code')
     CONTINUE_BUTTON=(By.ID, 'continue')




