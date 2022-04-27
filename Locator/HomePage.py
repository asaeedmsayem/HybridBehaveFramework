from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HomePage:
    loginXPath = "//a[@class='login_url']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.loginXPath).click()