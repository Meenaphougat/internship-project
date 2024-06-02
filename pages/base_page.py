from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open_url(self, url):
        logger.info(f'Opening {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f'Searching by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking by {locator}')
        self.find_element(*locator).click()

    # def input_text(self, text, *locator):
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(locator)
    #     )
    #     element.clear()
    #     element.send_keys(text)

    # adding to resolve some issue in firefox
    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by{locator}'
        ).click()

    def wait_until_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by{locator}'
        ).click()

    def wait_until_disappears(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by{locator}'
        ).click()

    def get_text_from_element(self, *locator):
        # Wait for the presence of the product name element
        product_name_element = self.wait.until(
            EC.presence_of_element_located(locator),
            message='Product name not present on the page'
        )
        # Get the text of the product name element and store it in the context or page object attribute
        return product_name_element.text

    # Window Handles
    def get_current_window(self):
        current_window = self.driver.current_window_handle
        print('Current window: ', current_window)
        print('All windows:', self.driver.window_handles)
        return current_window

    # def switch_new_window(self):
    #     self.wait.until(EC.new_window_is_opened)
    #     all_windows = self.driver.window_handles  # [Windows 1 , wind2 ...]
    #     print('All windows:', all_windows)
    #     print('Switching to this...', all_windows[1])
    #     self.driver.switch_to.window(all_windows[1])

    def switch_window_by_id(self, window_id):
        print('Switching to this...', window_id)
        self.driver.switch_to.window(window_id)

    # Verifications of all types
    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f"Expected {expected_text}, but got {actual_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contains {expected_partial_url}')

    def verify_url(self, expected_url):
        self.wait.until(EC.url_matches(expected_url), message=f'URL does not matches {expected_url}')

    # def verify_input_fields(self, locator):
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(locator), message=f'Input fields did not match {locator}'
    #     )
    #     text_message = element.get_attribute('value')
    #     print(f'The value of the input field is: {text_message}')

    def save_screenshot(self, name):
        self.driver.save_screenshot(f'{name}.png')

    def close_page(self):
        self.driver.close()
