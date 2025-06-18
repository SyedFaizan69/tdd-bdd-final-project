from behave import when, then
import requests

BASE_URL = "http://localhost:5000"

@when('I visit "{url}"')
def step_impl(context, url):
    """Send GET request to a URL"""
    context.response = requests.get(f"{BASE_URL}{url}")

@when('I DELETE "{url}"')
def step_impl(context, url):
    """Send DELETE request to a URL"""
    context.response = requests.delete(f"{BASE_URL}{url}")

@when('I PUT "{url}" with:')
def step_impl(context, url):
    """Send PUT request with JSON body"""
    headers = {"Content-Type": "application/json"}
    context.response = requests.put(f"{BASE_URL}{url}", data=context.text, headers=headers)

@then('the response status should be "{code}"')
def step_impl(context, code):
    """Check HTTP response status code"""
    assert context.response.status_code == int(code), f"Expected {code}, got {context.response.status_code}"

@then('the response should contain "{text}"')  # Task 7b
def step_impl(context, text):
    """Verify response contains text"""
    assert text in context.response.text, f'"{text}" not found in response.'

@then('the response should not contain "{text}"')  # Task 7c
def step_impl(context, text):
    """Verify response does NOT contain text"""
    assert text not in context.response.text, f'"{text}" should not be in response.'

@then('I should see the message "{message}"')  # Task 7d
def step_impl(context, message):
    """Check if a message is in the response (general use)"""
    assert message in context.response.text, f'Message "{message}" not found.'
