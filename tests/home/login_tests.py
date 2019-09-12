from selenium import webdriver
from login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):
    baseURL = "https://letskodeit.teachable.com/"
    driverLocation = "chromedriver.exe"
    driver = webdriver.Chrome(driverLocation)
    driver.maximize_window()
    driver.implicitly_wait(3)
    lp = LoginPage(driver)

    @pytest.mark.order2
    def test_validLogin(self):
        self.lp.clearFields()
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccess()
        assert result == True
        self.driver.quit()

    @pytest.mark.order1
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True