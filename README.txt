Project Link:
https://github.com/hilaab245-gif/newhilahome
How to run :
python main.py

How to Change Configuration:
Go to config.json file

design:
login
    login_page.py: login functionality
    open_url()-Navigates to the SauceDemo login page.
    login()-Insert the login action on a website
    click_login_button()-Submits the login form by clicking the login button and check if display error messages

test_1:The test1 directory contains four Python test files, each designed to validate a specific part
of the SauceDemo web application using Selenium automation
     1.shop.py-
     select_item()- function is designed to add the first three products displayed on
      the SauceDemo inventory page to the shopping cart.
      The checkout()-function completes the final step of the purchase process on the SauceDemo website
     sort_by_name_or_price() function is responsible for sorting the product list on the inventory page by name or by price
      -take the valur from a configuration file
      Add_to_Cart()-Select items that appear in the JSON file, but do not add them to the cart
        # if they are already present in the array we skip
      remove_to_Cart()-removed items that appear in the JSON file, but do not add to arr from function inventory.select_item()
        # if they are item already present in the array we skip
     2. OrderComplete.py-
      userdataorder()-function handles the process of entering user information during checkout on the SauceDemo website.
       It fills in the required fields: first name, last name, and postal code.
       clickonbutcontion()-function is responsible for clicking the Continue button on the checkout
       3.basic_fun-The basic_fun.py file contains two  functions that are used across multiple classes in the project.
       verify_page_title()-function checks whether the current page title matches an expected value
       error_mes()-Detects and returns error messages displayed on the page during form submission or validation.
       4.Checkout_page.py-
       verify_item- verify if the items match between cart and checkout
UI:
   Locator-Stores all UI element locators
 config:
    Base URL of the site, User Information,url and checkout data


Run output :
/Users/hila/miniconda3/bin/python /Users/hila/PycharmProjects/hilahometest/main.py
 Successfully opened URL: https://www.saucedemo.com/
 User successful to insert standard_user and password secret_sauce
Login button clicked successfully.
the user move to  Products page
 Added product #: Sauce Labs Backpack
 Added product #: Sauce Labs Bike Light
 Added product #: Sauce Labs Bolt T-Shirt
sort product list:
Sauce Labs Backpack
Sauce Labs Bike Light
Sauce Labs Bolt T-Shirt
Sauce Labs Fleece Jacket
Sauce Labs Onesie
Test.allTheThings() T-Shirt (Red)
Add to cart -select item from json file : Sauce Labs Fleece Jacket
Add to cart -select item from json file : Sauce Labs Onesie
not found all the item
remove item from  cart -select item from json file : Sauce Labs Fleece Jacket
remove item from  cart -select item from json file : Sauce Labs Onesie
not removed all the item
the user move to  Checkout: Your Information page
user data: Hila, Dalal, 123
the user move to  Checkout: Overview page
 All items match between cart and checkout.
 finish button clicked successfully.
the user move to  Checkout: Complete! page

