1.Project Link:
https://github.com/hilaab245-gif/newhilahome

2.How to run :
To start the application, run the following command:
python main.py

3.How to Change Configuration:
Configuration settings can be modified in the config.json file


4.Design Overview
#login folder-
    login_page.py: all login-related functionality for the SauceDemo website.
    open_url()-Navigates to the SauceDemo login page.
    login()-Insert the login action on a website
    click_login_button()-Submits the login form by clicking the login button and check if display error messages

#test_1:The test1 directory contains four Python test files, each designed to validate a specific part
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
UI folder:
   Locator-Stores all UI element locators
 
 config.JSON:
   The `config.json` file contains essential settings used throughout the project:
 -Base URL  - The  address of the website (e.g., `https://www.saucedemo.com`).
- User Information - Login credentials such as username and password.
- Checkout Data -  Data required for the checkout process.
- - Product - List of product names.
- SortSorting preferences for product listings (e.g., by price, name).

Main.py -
- `load_config()-Loads the `config.json` file using the  function and Extracts key parameters/
-  Calls functions from `login_page.py`, Checkout and Payment, and Inventory


Run output :

successful run output:
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

 Failure run: 
 python main.py
 Successfully opened URL: https://www.saucedemo.com/
 User successful to insert standard_user1 and password secret_sauce
Login button clicked successfully.
 Error mes: Epic sadface: Username and password do not match any user in this service
WARNING:root: Login failed : Epic sadface: Username and password do not match any user in this service

כש

 כשן
the user move to  Checkout: Complete! page

