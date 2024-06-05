from allure_commons import fixture
from behave import use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from pages.base_page import Page
from datetime import datetime
from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # Chrome browser mode
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # Firefox browser mode
    # gecko_driver_path = GeckoDriverManager().install()
    # options = webdriver.FirefoxOptions()
    # options.headless = True  # Run Firefox in headless mode (optional)
    # # Customize additional Firefox options as needed
    # options.add_argument('--disable-infobars')
    # options.add_argument('--disable-extensions')
    # service = Service(gecko_driver_path)
    # context.driver = webdriver.Firefox(service=service, options=options)

    # # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--window-size=1920,1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'meena_ReZygC'
    bs_key = 'GBu3zqpppyhRxjwDeHvU'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'chrome',
        'sessionName': 'Test Scenarios for Search functionality of soft.reelly page'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
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

    # Cleanup
    context.driver.delete_all_cookies()
    context.driver.quit()
