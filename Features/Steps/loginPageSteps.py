import allure
import time
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Locator.HomePage import HomePage
from Locator.loginPage import loginPage
from Utilities.customLogger import LogGen
from Utilities.readProperty import readConfig

baseURL = readConfig.getURL()
mylogger = LogGen.loggen()

@when(u'Enter login credential')
def step_impl(context):
    global hpage
    global lpage
    mylogger.info("*** Entering Login Credential ***")
    hpage = HomePage(context.driver)
    hpage.clickOnLogin()
    lpage = loginPage(context.driver)
    user = readConfig.getUsername()
    pwas = readConfig.getPassword()
    lpage.typeUsername(user)
    lpage.typePassword(pwas)
    time.sleep(5)

@when(u'Click login button')
def step_impl(context):
    lpage.clickLogin()
    mylogger.info("*** Login Clicked ***")

@then(u'Verify the page title and take screenshot')
def step_impl(context):
    actualTitle = context.driver.title
    expectedTitle = "Login – Change 2 Automation"
    if actualTitle == expectedTitle:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\"+"LoginPage Verified.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Login Verification Test", attachment_type=AttachmentType.PNG)
        mylogger.info("*** LoginPage Title Match Verified")
    else:
        mylogger.info("*** LoginPage Title Not Matched")
        context.driver.save_screenshot(".\\Screenshots\\"+"LoginPage Verification Failed.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="Login Verification Test", attachment_type=AttachmentType.PNG)
        assert False
        time.sleep(5)


@then(u'Close the app')
def step_impl(context):
    context.driver.quit()
    mylogger.info("*** Browser Closed ***")
