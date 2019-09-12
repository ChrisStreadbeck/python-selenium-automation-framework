from selenium.webdriver.common.by import By
from selenium_driver import SeleniumDriver
import logging

import custom_logger as cl

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    
    # Actions
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)
    
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    # Use Actions
    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccess(self):
        result = self.isElementPresent("//*[@id=\"navbar\"]//img[@class=\"gravatar\"]", locatorType="xpath")
        return result
       