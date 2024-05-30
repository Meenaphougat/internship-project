from pages.edit_profile_page import EditProfilePage
from pages.base_page import Page
from pages.sign_In_page import SignInPage



class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.edit_profile_page = EditProfilePage(driver)
        self.sign_In_page = SignInPage(driver)

