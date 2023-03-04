import logging
import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Loginpage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.searchCustomerPage import searchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration

class Test_005_searchCustomerByName:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGeneration.logGen()


    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("********* searchCustomerByName_005 *********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login successful ******")
        self.logger.info("********** starting search customer by Name*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(3)
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("******* searching customer by Name********")
        searchCust = searchCustomer(self.driver)

        searchCust.setFirstName("Victoria")
        searchCust.setLastName("Terces")
        searchCust.clickSearch()
        time.sleep(4)
        status = searchCust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("************************TC_SearchCustomerByName_005 Finished ******************************************")