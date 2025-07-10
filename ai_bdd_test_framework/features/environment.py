from playwright.sync_api import sync_playwright
from utils.types import CustomContext
import json
import logging
import allure # type: ignore
from allure_commons.types import AttachmentType # type: ignore

#Set up logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def before_all(context: CustomContext):
   # This function is called before all tests start
   logger.info("Starting Playwright....")

   # Load environment variables from env.json
   with open('config/env.json', 'r') as file:
       env_vars = json.load(file)

   # Accessing variables from env.json  
   browser_type = env_vars.get("browser", "chromium")
   headless_mode = env_vars.get("headless", False)

   context.playwright = sync_playwright().start()
   context.browser = context.playwright[browser_type].launch(headless=headless_mode, args=["--start-maximized"])

def before_scenario(context: CustomContext, scenario):
    # This function is called before each scenario
    logger.info(f"Starting Scenario: {scenario.name}")
    context.page = context.browser.new_page(no_viewport=True) # Create a new page for the scenario

def after_scenario(context: CustomContext, scenario):
    # This function is called after each scenario   
    
    # Capture screenshot on failure
    if scenario.status == "failed":
        # Capture screenshot on failure
        screenshot_path = f"screenshots/{scenario.name.replace(' ', '_')}.png"
        context.page.screenshot(path=screenshot_path)
        logger.info(f"Captures screenshot for failed Scenario: {screenshot_path}")

        # Attach screenshot to Allure reports
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=scenario.name, attachment_type=AttachmentType.PNG)


    logger.info(f"Ending Scenario: {scenario.name}")
    context.page.wait_for_timeout(2000)
    context.page.close()

def after_all(context: CustomContext):
    # This function is called after all tests have finished
    logger.info("Stopping Playwright....")
    context.browser.close() # Close the browser
    context.playwright.stop() # Stop the Playwright instance