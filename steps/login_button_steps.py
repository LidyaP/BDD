from behave import *


@given('I am on the MokFlow homepage and i want to intiate the login process with invalid password')
def step_impl(context):
    context.home_page.open_home_page()


@when('I click on login button')
def step_impl(context):
    context.home_page.click_login_button()


@when('I enter my valid email')
def step_impl(context):
    context.home_page.insert_email()


@when('I enter my invalid "{user_password}"')
def step_impl(context, user_password):
    context.home_page.insert_invalid_password(user_password)


@when('I click on Sign In')
def step_impl(context):
    context.home_page.click_singin_button()


@then('I receive an "{error_message}"')
def step_impl(context, error_message):
    context.home_page.login_failed(error_message)


@when('I enter my valid password')
def step_impl(context):
    context.home_page.insert_password()


@when('I click on Sign In button')
def step_impl(context):
    context.home_page.click_singin_button()


@then('I am redirected to my account page')
def step_impl(context):
    context.home_page.my_account_page()