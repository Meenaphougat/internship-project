from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CLICK_SAVE = (By.XPATH, "//div[contains(text(), 'Save changes')]")
CLICK_CLOSE = (By.XPATH, "//div[contains(@class, 'profile-button-block') and contains(., 'Close')]")
#CLICK_EDIT_PROFILE = (By.XPATH, "//div[contains(@class, 'setting-text') and text()='Edit profile']")
CLICK_EDIT_PROFILE = (By.XPATH, "//a[@href='/profile-edit' and contains(@class, 'page-setting-block')]")
INPUT_FIELD_JOIN_COMP = (By.ID, "When-joined-company-2")


@then('Click on settings open')
def click_on_settings(context):
    context.app.edit_profile_page.click_setting_options()


@then('Click on Edit profile option')
def edit_profile(context):
    context.app.base_page.wait_until_clickable(*CLICK_EDIT_PROFILE)
    sleep(4)


@when('Enter some test information in the input fields')
def input_fields(context):
    context.app.edit_profile_page.input_fields()
    sleep(3)


@then('Check the right information is present in the input fields')
def verify_input_fields(context):
    context.app.edit_profile_page.verify_input_fields()


@then('Click on Save changes')
def click_on_save(context):
    context.app.base_page.wait_until_clickable(*CLICK_SAVE)


@then('Click on Close')
def click_on_save(context):
    context.app.base_page.wait_until_clickable(*CLICK_CLOSE)

