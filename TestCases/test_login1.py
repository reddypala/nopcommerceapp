import logging
import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration

class Test_001_Login:

    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGeneration.logGen()


    @pytest.mark.regression
    def test_homePage_title(self,setup):
        self.logger.info("************** Test_001_Login **************")
        self.logger.info("************** verifying homepage title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        time.sleep(3)

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************** Homepage title is matched with expected title **************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePage_title.png")
            self.driver.close()
            self.logger.error("************** Homepage title is not matched with expected title **************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************** verfying login test **************")
        self.logger.info("************** verfying for login page title  **************")
        self.driver  = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        time.sleep(3)
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("************** loginpage title is  matched with expected title **************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("************** Loginpage title is  not matched with expected title **************")
            assert False

