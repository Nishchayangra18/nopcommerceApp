import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData_nopCommerceApp.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_ddt(self, Setup):
        self.logger.info("********************** Test_002_DDT_Login  ************************")
        self.logger.info("********************** Verifying Login DDT Test  ************************")
        self.driver = Setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Login')
        print("Number of rows in excel", self.rows)

        list_status = []             # Empty list variable

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Login', r, 1)
            self.password = XLUtils.readData(self.path, 'Login', r, 2)
            self.exp = XLUtils.readData(self.path, 'Login', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Passed *****")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***** Failed *****")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Failed *****")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***** Passed *****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("Login DDT Test case passed.....")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Test case failed.....")
            self.driver.close()
            assert False

        self.logger.info("********************** End of Login DDT Test  ************************")
        self.logger.info("********************** Completed Test_002_DDT_Login ************************")


