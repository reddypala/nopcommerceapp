import logging
import random
import string
import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Loginpage
from PageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGeneration.logGen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*********Test_003_AddCustomer*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful ********")

        self.logger.info("****** Starting Add Customers Test *******")
        # instantiating the addcustomers page
        self.addcust = AddCustomer(self.driver)

        self.addcust.clickOnCustomersMenu()
        time.sleep(3)
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clcikOnAddNew()

        self.logger.info("******* Providing customer details **********")
        self.email = random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("krishna")
        self.addcust.setLastName("hari")
        self.addcust.selectGender("Male")

        self.addcust.setDOB("7/05/1985")
        self.addcust.setCompanyName("busyQA")
        time.sleep(3)
        self.addcust.setCustomerRoles("Vendors")
        self.addcust.setManagerVendor("Vendor 2")

        self.addcust.clickSaveBtn()

        self.logger.info("********* saving customer info *****")

        self.logger.info("*********** Add customer validation started")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("******* Add customer test passed******")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_addCustomer_scr.png")
            self.logger.error("***** Add Customer test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("*************** End of the Add Customer Test **********")




def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

