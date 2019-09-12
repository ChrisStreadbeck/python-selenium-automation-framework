from selenium import webdriver
import unittest

from login_page import LoginPage

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driverLocation = "chromedriver.exe"
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        
        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        result = lp.verifyLoginSuccess()

        assert result == True

        driver.quit()
        