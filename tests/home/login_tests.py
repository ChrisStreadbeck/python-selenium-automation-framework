from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import logging

import custom_logger as cl
from login_page import LoginPage

class LoginTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def test_validLogin(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        
        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH, "//*[@id=\"navbar\"]//img[@class=\"gravatar\"]")

        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")
