import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities import ExcelUtilityFile

class Test_002_DDTLogin:

    baseURL = ReadConfig.getApplicationUrl()
    path = ".//TestData//datasheet.xlsx"
    logger = LogGeneration.logGen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_ddtLogin******")
        self.logger.info("************** verfying login test **************")
        self.logger.info("************** verfying for login page title  **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)

        self.rows = ExcelUtilityFile.getRowCount(self.path,'logindata')
        print("Number of rows in a Excel:",self.rows)

        test_status=[]         # Empty List

        for r in range(2,self.rows+1):
            self.user = ExcelUtilityFile.readData(self.path,'logindata',r,1)
            self.password = ExcelUtilityFile.readData(self.path,'logindata',r,2)
            self.exp = ExcelUtilityFile.readData(self.path,'logindata',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("******** test is passed ******")
                    self.lp.clickLogout()
                    test_status.append("PASS")
                elif self.exp == "fail":
                    self.logger.info("******** test is failed ******")
                    self.lp.clickLogout()
                    test_status.append("FAIL")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("****failed****")
                    test_status.append("FAIL")

                elif self.exp == "fail":
                    self.logger.info("******** passed *********")
                    test_status.append("PASS")


        if "FAIL" not in test_status:
            self.logger.info("Login ddt test is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login ddt test is failed")
            self.driver.close()
            assert False

        self.logger.info("*********End of the login data driven test**************")
        self.logger.info("*********Completed Login DDT Testcase**************")