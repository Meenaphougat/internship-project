from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(Page):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[class="login-button w-button"]')
    RELLY_EMAIL = (By.CSS_SELECTOR, "[id*='email-2']")
    RELLY_PASSWORD = (By.CSS_SELECTOR, "[id*='field']")

    def open_main(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def click_sign_in(self):
        self.click(*self.CONTINUE_BUTTON)
        sleep(5)

    def input_credentials(self):
        self.input_text('meenaphougat23@gmail.com', *self.RELLY_EMAIL)
        self.input_text('Prisha@0113', *self.RELLY_PASSWORD)
