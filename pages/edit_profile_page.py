from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class EditProfilePage(Page):
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    INPUT_FIELD_VERIFICATION = (By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    INPUT_FIELD = (By.XPATH, "//input[contains(@class, 'field-form-block w-input') and contains(@name, 'Languages')]")
    INPUT_FIELD_JOIN_COMP = (By.ID, "When-joined-company-2")

    def __init__(self, driver):
        super().__init__(driver)
        self.default_pw = 'Password'

    def input_fields(self):
        # self.input_text('2024', *self.INPUT_FIELD_JOIN_COMP)
        # sleep(5)
        self.input_text('2024', *self.INPUT_FIELD_JOIN_COMP)

    def verify_input_fields(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.INPUT_FIELD_JOIN_COMP)
        )


