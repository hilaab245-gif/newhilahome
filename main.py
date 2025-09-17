import json
import logging
import sys
from pathlib import Path
from login.login_page import LoginPage
from test_1.shop import InventoryPage
from test_1.OrderComplete import OrderCompleteclass
from test_1.Checkout_page import Checkoutclass
CONFIG_PATH = Path("config.json")

#load json config
with open(CONFIG_PATH, "r") as config_file:
    CONFIG = json.load(config_file)
def load_config(path: Path) -> dict:
    if not path.exists():
        logging.error("Config file not found: %s", path)
        raise FileNotFoundError(f"Missing config file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    try:
        config = load_config(CONFIG_PATH)

        # Extract config values
        base_url = config.get("base_url")
        username = config.get("username")
        password = config.get("password")
        sort_d = config.get("sort_by")
        checkout = config.get("checkout", {})
        first_name = checkout.get("first_name")
        last_name = checkout.get("last_name")
        zip_code = checkout.get("zip_code")

        # Login using the default credentials
        page = LoginPage()
        page.open_url(base_url)
        page.login(username, password)
        page.click_login_button()


        # Select 3 items and add them to the shopping cart.
        inventory = InventoryPage(page.driver)
        orderitem=inventory.select_item()
        inventory.sort_by_name_or_price(sort_d)
        inventory.checkout()

        # user payment
        order = OrderCompleteclass(inventory.driver)
        order.userdataorder(first_name, last_name, zip_code)
        order.clickonbutcontion()

        #Complete order
        check=Checkoutclass(order.driver)
        check.verify_item(orderitem)
        check.click_finish_button()
        sys.exit(0)
    except Exception as e:
               logging.exception("An error occurred during execution: %s", e)
    finally:
        if 'page' in locals():
            page.driver.quit()


if __name__ == "__main__":
    main()
