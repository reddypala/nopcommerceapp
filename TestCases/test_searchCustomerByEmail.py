import logging
import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Loginpage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.searchCustomerPage import searchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration

class Test_004_searchCustomerByEmail:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGeneration.logGen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("********* searchCustomerByEmail_004 *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successful ******")
        self.logger.info("********** starting search customer by emailId*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(3)
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("******* searching customer by emailId********")
        searchCust = searchCustomer(self.driver)
        searchCust.setEmail("victoria_victoria@nopCommerce.com")
        searchCust.clickSearch()
        time.sleep(5)
        status = searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("************************TC_SearchCustomerByEmail_004 Finished ******************************************")
