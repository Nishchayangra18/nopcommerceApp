import random
import string
import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from pageObjects.Add_Customer_Page import CustomerPage
from selenium.webdriver.common.by import By
from pageObjects.Search_Customer_Page import SearchCustomerPage


class Test_004_Search_CustomerbyEmail:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData_nopCommerceApp.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchcustomerbyemail(self, Setup):
        self.logger.info("********************** Test_004_Search_CustomerbyEmail  ************************")

        self.driver = Setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows_login = XLUtils.getRowCount(self.path, 'Login')

        self.user = XLUtils.readData(self.path, 'Login', 2, 1)
        self.password = XLUtils.readData(self.path, 'Login', 2, 2)

        self.lp.setUsername(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******************** Login Successful ************************")
        time.sleep(10)
        self.logger.info("********************** Starting Search Customer by email Test ************************")

        self.addcust = CustomerPage(self.driver)
        self.addcust.ClickCustomerMenu()
        self.addcust.ClickCustomerMenuItem()
        self.addcust.clickAddnewbutton()
        self.logger.info("***************** Providing customer info****************")

        self.rows_customer = XLUtils.getRowCount(self.path, 'Customer_info')

        for r in range(2, self.rows_customer + 1):
            self.email = XLUtils.readData(self.path, 'Customer_info', r, 11)
            self.password = XLUtils.readData(self.path, 'Customer_info', r, 1)
            self.firstname = XLUtils.readData(self.path, 'Customer_info', r, 2)
            self.lastname = XLUtils.readData(self.path, 'Customer_info', r, 3)
            self.gender = XLUtils.readData(self.path, 'Customer_info', r, 4)
            # self.dob = XLUtils.readData(self.path, 'Customer_info', r, 5)
            self.company = XLUtils.readData(self.path, 'Customer_info', r, 6)
            # self.newsletter = XLUtils.readData(self.path, 'Customer_info', r, 7)
            self.role = XLUtils.readData(self.path, 'Customer_info', r, 8)
            self.vendor = XLUtils.readData(self.path, 'Customer_info', r, 9)
            self.comment = XLUtils.readData(self.path, 'Customer_info', r, 10)

            self.addcust.Setemail(self.email)
            self.addcust.setPassword(self.password)
            self.addcust.setFirstname(self.firstname)
            self.addcust.setLastname(self.lastname)
            self.addcust.selectGender(self.gender)
            self.addcust.setDob("10/18/1998")
            self.addcust.setCompanyname(self.company)
            # self.addcust.setNewsletter(self.newsletter)
            self.addcust.setCustomerRole(self.role)
            self.addcust.setManagerOfVendor(self.vendor)
            self.addcust.setComment(self.comment)
            self.addcust.clickSave()

            self.logger.info("********************** Searching customer by email *******************************")
            searchcust = SearchCustomerPage(self.driver)
            searchcust.Enteremail(self.email)
            searchcust.ClickRegisteredcrossbutton()
            searchcust.ClickSearchbutton()
            time.sleep(5)
            status = searchcust.SearchCustomerbyEmail(self.email)
            assert True == status

            if r < self.rows_customer:
                self.addcust.clickAddnewbutton()

        self.logger.info("********************** Searching customer by email Passed *******************************")
        self.logger.info("********************** Test_004_Search_CustomerbyEmail Completed ************************")