from behave import given, when, then
from time import sleep


@given('Open soft reelly main page')
def open_soft_reelly(context):
    context.app.sign_In_page.open_main()
    sleep(5)


@given('Login to the page')
def input_credentials(context):
    context.app.sign_In_page.input_credentials()


@then('Click on continue button')
def click_search_icon(context):
    context.app.sign_In_page.click_sign_in()
