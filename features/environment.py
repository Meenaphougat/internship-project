from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from pages.base_page import Page
from datetime import datetime
from app.application import Application
from support.logger import logger


#  How to Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_ui_tests.feature
# If we want to use tags
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ -t smoke

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed: {step}')
        context.app.base_page.save_screenshot(step)


def after_scenario(context, feature):
    if feature.status == "passed":
        # Generate screenshot filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_file = f"screenshot_{timestamp}.png"

        # Take screenshot and save it
        context.driver.save_screenshot(screenshot_file)
        print(f"Screenshot captured: {screenshot_file}")

    #Clean up
    context.driver.delete_all_cookies()
    context.driver.quit()
