from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('I am on the Demo Login Page')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account {user} into the Username field and the Password field')
def step_impl(context, user):
    credentials = {
        "StandardUser": ("standard_user", "secret_sauce"),
        "LockedOutUser": ("locked_out_user", "secret_sauce")
    }
    username, password = credentials[user]
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)

@when('I click the Login Button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('I am redirected to the Demo Main Page')
def step_impl(context):
    assert "inventory.html" in context.driver.current_url

@then('I verify the App Logo exists')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, "app_logo").is_displayed()

@then('I verify the Error Message contains the text "Sorry, this user has been banned."')
def step_impl(context):
    error_message = context.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Epic sadface: Sorry, this user has been locked out." in error_message

@given('I am on the inventory page')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.saucedemo.com/inventory.html")

@when('user sorts products from high price to low price')
def step_impl(context):
    select = Select(context.driver.find_element(By.CLASS_NAME, "product_sort_container"))
    select.select_by_value("hilo")

@when('user adds highest priced product')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]").click()

@when('user clicks on cart')
def step_impl(context):
    context.driver.find_element(By.ID, "shopping_cart_container").click()

@when('user clicks on checkout')
def step_impl(context):
    context.driver.find_element(By.ID, "checkout").click()

@when('user enters first name {first_name}')
def step_impl(context, first_name):
    context.driver.find_element(By.ID, "first-name").send_keys(first_name)

@when('user enters last name {last_name}')
def step_impl(context, last_name):
    context.driver.find_element(By.ID, "last-name").send_keys(last_name)

@when('user enters zip code {zip_code}')
def step_impl(context, zip_code):
    context.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

@when('user clicks Continue button')
def step_impl(context):
    context.driver.find_element(By.ID, "continue").click()

@then('I verify in Checkout overview page if the total amount for the added item is $49.99')
def step_impl(context):
    total_price = context.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    assert "$49.99" in total_price

@when('user clicks Finish button')
def step_impl(context):
    context.driver.find_element(By.ID, "finish").click()

@then('Thank You header is shown in Checkout Complete page')
def step_impl(context):
    thank_you_header = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in thank_you_header

def after_scenario(context, scenario):
    context.driver.quit()