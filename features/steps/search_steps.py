import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I navigate to google.com')
def step_impl(context):

    context.driver.get("http://google.com")
    context.driver.implicitly_wait(2)
    context.driver.find_element("xpath", "//button[@id='L2AGLb']").click()
    #input()
    context.driver.implicitly_wait(1)


@when(u'I validate the page title')
def step_impl(context):
    title = context.driver.title
    print("Title is " + title)
    time.sleep(4)
    assert "Google" in title



@then(u'I enter the text as "{searchText}"')
def step_impl(context,searchText):
    context.driver.find_element("name", "q").send_keys(searchText)


@then(u'I click the search button')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@title='Search']").click()
    time.sleep(3)
