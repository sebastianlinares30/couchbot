from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

"""
This module handles the automation service for Supreme using Selenium WebDriver. 
It parses configuration data and executes a multi-step checkout workflow.
"""

class SupremeService:
    def __init__(self, data):
        """
        Initializes the service with target item, shipping, and billing parameter information.
        Extracts from the incoming JSON payload.
        """
        # Item info
        self.item_type = data.get('type')
        self.item_name = data.get('name')
        self.item_color = data.get('color')
        self.item_size = data.get('size')
        
        # Checkout info
        self.first_name = data.get('firstName')
        self.last_name = data.get('lastName')
        self.address = data.get('address')
        self.apt = data.get('apt')
        self.city = data.get('city')
        self.state = data.get('state')
        self.zip_code = data.get('zip')
        self.email = data.get('email')
        self.phone = data.get('phone')
        
        # Card info
        self.card_name = data.get('cardName')
        self.card_number = data.get('cardNumber')
        self.card_expiry = data.get('cardExpiry')
        self.card_security = data.get('cardSecurity')

    def run_checkout(self):
        """
        Orchestrates the entire bot execution flow by initializing the driver 
        and sequentially invoking each modular automation step.
        """
        driver = webdriver.Chrome()

        try:
            self._open_store_and_navigate(driver)
            self._select_and_add_item(driver)
            self._fill_shipping_details(driver)
            self._fill_payment_details(driver)
            self._finalize_and_close(driver)
        finally:
            driver.quit()

    def _open_store_and_navigate(self, driver):
        """
        Launches the browser, loads the base URL, and navigates through to the all product view.
        """
        driver.get("https://supreme.com/")

        # Navigate to shop page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shop"))
        ).click()

        # Navigate to all products
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "view all"))
        ).click()

    def _select_and_add_item(self, driver):
        """
        Filters by item category, finds specific product, and matches color/size.
        Adds the item to the cart and clicks through to the checkout page.
        """
        # Navigate to product type
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.item_type))
        ).click()

        # Navigate to specific product
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.item_name))
        ).click()

        # Navigate to product color
        color_xpath = f"//button[contains(@title, '{self.item_name} - {self.item_color}')]"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, color_xpath))
        ).click()

        # Select size drop-down
        size_select = Select(
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.NAME, "size"))
            )
        )
        size_select.select_by_visible_text(self.item_size)

        # Add item to cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-to-cart-button']"))
        ).click()

        # Navigate to checkout page
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "checkout now"))
        ).click()

    def _fill_shipping_details(self, driver):
        """
        Fills in all required customer information, contact information, and shipping address.
        """
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        ).send_keys(self.email)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        ).send_keys(self.first_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "lastName"))
        ).send_keys(self.last_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "address1"))
        ).send_keys(self.address)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "address2"))
        ).send_keys(self.apt or "")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "city"))
        ).send_keys(self.city)

        state_select = Select(
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "zone"))
            )
        )
        state_select.select_by_visible_text(self.state)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "postalCode"))
        ).send_keys(self.zip_code)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        ).send_keys(self.phone)

    def _fill_payment_details(self, driver):
        """
        Iterates through payment iframes (card number, expiration, security code, and name) to input billing details.
        """
        # Card number iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.card-fields-iframe[id*='number']")
            )
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "number"))
        ).send_keys(self.card_number)
        driver.switch_to.default_content()

        # Expiry iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.card-fields-iframe[id*='expiry']")
            )
        )
        expiry_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "expiry"))
        )
        for ch in self.card_expiry.replace('/', ''):
            expiry_input.send_keys(ch)
            time.sleep(0.2)
        driver.switch_to.default_content()

        # Security code iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.card-fields-iframe[id*='verification_value']")
            )
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "verification_value"))
        ).send_keys(self.card_security)
        driver.switch_to.default_content()

        # Card name iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe.card-fields-iframe[id*='name']")
            )
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        ).send_keys(self.card_name)
        driver.switch_to.default_content()

    def _finalize_and_close(self, driver):
        """
        Pauses briefly to let final transactions register and safely terminates the browser session.
        """
        time.sleep(10)
        driver.quit()