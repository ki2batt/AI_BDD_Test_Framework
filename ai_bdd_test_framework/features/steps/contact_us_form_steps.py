from behave import given, when, then
from utils.types import CustomContext
import logging
from playwright.sync_api import TimeoutError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('verify_logger')

@given('I am on the Contact Us form')
def navigate_to_contact_us_form(context: CustomContext):
    context.page.goto("https://webdriveruniversity.com/Contact-Us/contactus.html")

@when('I fill in the "{field}" field with "{value}"')
def fill_in_field(context: CustomContext, field, value):
    field_selector = f'[name="{field}"]'

    if value == "\\n":
        logger.info(f"Skipping field {field} as indicated by '\\n'.")
        return
    
    context.page.wait_for_selector(field_selector)
    context.page.fill(field_selector, value)
    logger.info(f"Filled field {field} with data {value}")

@when('I click on the "{button}" button')
def click_button(context: CustomContext, button):
    button_selector = f'[value="{button}"]'
    context.page.wait_for_selector(button_selector)
    context.page.click(button_selector)

@then('I should see the success message saying "{message}"')
def verify_success_message(context: CustomContext, message):
    success_message_selector = f'//*[contains(text(), "{message}")]'
    try:
        logger.info(f"Waiting for success message: {message}")
        context.page.wait_for_selector(success_message_selector, timeout=2000)
        assert context.page.is_visible(success_message_selector)
        logger.info(f"Success Message: {message} is visible!")
    except TimeoutError:
        logger.error(f"Success Message: {message} not found!!")
        assert False, f"Success message '{message}' not found on the page"

@then('I should see an error message saying "{message}"')
def verify_error_message(context: CustomContext, message):
    error_message_selector = f'//body[contains(., "{message}")]'
    try:
        logger.info(f"Waiting for error message: {message}")
        context.page.wait_for_selector(error_message_selector, timeout=2000)
        assert context.page.is_visible(error_message_selector)
        logger.info(f"Error Message: {message} is visible!")
    except TimeoutError:
        logger.error(f"Error Message: {message} not found!!")
        assert False, f"Error message '{message}' not found on the page"

@then('all fields should be cleared')
def verify_all_fields_cleared(context: CustomContext):
    field_selectors = ['[name="first_name"]', '[name="last_name"]', '[name="email"]', '[name="message"]']

    for field_selector in field_selectors:
        field_value = context.page.locator(field_selector).input_value()
        assert field_value == "", f"Field {field_selector} is not cleared"

    logger.info("All fields are cleared!")  


@then('I should see the message "{expected_message}"')
def verify_message(context: CustomContext, expected_message):
    message_selector = f'//*[contains(text(), "{expected_message}")] | //body[contains(., "{expected_message}")]'
    try:
        logger.info(f"Waiting for message: {expected_message}")
        context.page.wait_for_selector(message_selector, timeout=2000)
        assert context.page.is_visible(message_selector)
        logger.info(f"Message: {expected_message} is visible!")
    except TimeoutError:
        logger.error(f"Message: {expected_message} not found!!")
        assert False, f"Message '{expected_message}' not found on the page" 