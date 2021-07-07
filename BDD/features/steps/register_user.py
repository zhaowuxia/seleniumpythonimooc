from behave import *
use_step_matcher('re')
@when('open register website"([^'']*)"')
def step_register(context,url):
    context.driver.get(url)
@then('I expect that the title is "([^'']*)"')
def step_register(context,title_name):
    title = context.driver.title
    assert title_name in title