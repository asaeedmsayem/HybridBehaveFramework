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

@given(u'Launch the browser and open the app')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("*** Driver Initialized ***")
    context.driver.get(baseURL)
    mylogger.info("*** Browser Launched ***")

@then(u'Verify page title')
def step_impl(context):
    actualTitle = context.driver.title
    expectedTitle = "Change 2 Automation – Change 2 Automation"
    if actualTitle == expectedTitle:
        assert True
        mylogger.info("*** HomePage Title Match Verified")
    else:
        mylogger.info("*** HomePage Title Not Matched")
        assert False
        time.sleep(5)

@then(u'Quit the browser')
def step_impl(context):
    context.driver.quit()
    mylogger.info("*** Browser Closed ***")
