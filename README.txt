Project Link:

How to run :
python main.py

How to Change Configuration:
Go to config.json file
you can change User Information,url and checkout

design:
login
    login_page.py: login functionality-entering username and password, clicking the login button, and verifying successful navigation to the next page.
test_1:
     OrderComplete.py-Fills in user information and Verifies that the user reaches the order confirmation page
     shpp.py- Selects 3 products that are not already in the cart

UI:
   Locator-Stores all UI element locators
 config:
    Base URL of the site, User Information,url and checkout data
Run output :
/Users/hila/miniconda3/bin/python /Users/hila/PycharmProjects/hilahometest/main.py
 Successfully opened URL: https://www.saucedemo.com/
 Login successful user standard_user and password secret_sauce
Login button clicked successfully.
 Products page loaded successfully
 Added product #: Sauce Labs Backpack
 Added product #: Sauce Labs Bike Light
 Added product #: Sauce Labs Bolt T-Shirt
user data: Hila, Dalal, 12345
https://www.saucedemo.com/checkout-step-two.html
 Order completed successfully — on the correct page

Process finished with exit code 0
