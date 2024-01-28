from behave import *

@given('I am logged into my account')
def step_impl(context):
    context.home_page.open_home_page()
    context.home_page.click_login_button()
    context.home_page.insert_email()
    context.home_page.insert_password()
    context.home_page.click_singin_button()

@when('I see the offer')
def step_impl(context):
    context.my_wireframe_page.i_see_the_offer


@when('I click on x button')
def step_impl(context):
    context.my_wireframe_page.close_the_offer


@then('The offer is closed')
def step_impl(context):
    context.my_wireframe_page.offer_is_closed
