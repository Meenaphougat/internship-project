from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import (expected_conditions as EC)


class EditProfilePage(Page):
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    INPUT_FIELD_VERIFICATION = (By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    INPUT_FIELD = (By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    INPUT_FIELD_JOIN_COMP = (By.CSS_SELECTOR, "input#When-joined-company-2")
    CLICK_SETTINGS = (By.XPATH, "//div[contains(@class, 'menu-button-text') and text()='Settings']")

    def __init__(self, driver):
        super().__init__(driver)
        #self.default_pw = 'Password'

    def input_fields(self):
        try:
            # Wait for the input field to be visible
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.INPUT_FIELD_JOIN_COMP)
            )
            # Input the text into the field
            input_field.clear()  # Clear existing text (if any)
            input_field.send_keys('2024')
        except TimeoutException:
            # Handle the timeout gracefully
            print("Timeout occurred while waiting for the input field to be visible.")
            # You can add logging or other error handling here
            raise  # Re-raise the exception to fail the test

        # Optionally, add a sleep if necessary
        sleep(5)

    # Adding for Firefox instead of above
    def verify_input_fields(self):
        input_value = '2024'
        # Wait for the input field to be present
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.INPUT_FIELD_JOIN_COMP)
        )
        # Verify that the input field contains the expected value
        input_field_value = element.get_attribute('value')
        assert input_field_value == input_value, f"Input field value does not match expected value: {input_field_value}"

    def click_setting_options(self):
        setting_options_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.CLICK_SETTINGS))
        setting_options_button.click()
        sleep(10)
