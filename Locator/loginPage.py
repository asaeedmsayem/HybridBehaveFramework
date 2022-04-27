from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class loginPage:
    UserXpath = "//input[@id='username']"
    PassXpath = "//input[@id='password']"
    LoginButtonXpath = "//button[contains(text(),'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def typeUsername(self, User):
        self.driver.find_element_by_xpath(self.UserXpath).send_keys(User)

    def typePassword(self, Pass):
        self.driver.find_element_by_xpath(self.PassXpath).send_keys(Pass)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.LoginButtonXpath).click()