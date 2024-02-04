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


class Test_003_Add_Customer:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData_nopCommerceApp.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_customer(self, Setup):
        self.logger.info("********************** Test_003_Add_Customer  ************************")

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
        self.logger.info("********************** Starting Add Customer Test  ************************")

        self.addcust = CustomerPage(self.driver)
        self.addcust.ClickCustomerMenu()
        self.addcust.ClickCustomerMenuItem()
        self.addcust.clickAddnewbutton()
        #self.addcust.customerInfo_xpath()

        self.logger.info("***************** Providing customer info****************")

        self.rows_customer = XLUtils.getRowCount(self.path, 'Customer_info')

        for r in range(2, self.rows_customer + 1):

            self.password = XLUtils.readData(self.path, 'Customer_info', r, 1)
            self.firstname = XLUtils.readData(self.path, 'Customer_info', r, 2)
            self.lastname = XLUtils.readData(self.path, 'Customer_info', r, 3)
            self.gender = XLUtils.readData(self.path, 'Customer_info', r, 4)
            #self.dob = XLUtils.readData(self.path, 'Customer_info', r, 5)
            self.company = XLUtils.readData(self.path, 'Customer_info', r, 6)
            #self.newsletter = XLUtils.readData(self.path, 'Customer_info', r, 7)
            self.role = XLUtils.readData(self.path, 'Customer_info', r, 8)
            self.vendor = XLUtils.readData(self.path, 'Customer_info', r, 9)
            self.comment = XLUtils.readData(self.path, 'Customer_info', r, 10)

            self.email = random_generator() + "@gmail.com"
            self.addcust.Setemail(self.email)
            self.addcust.setPassword(self.password)
            self.addcust.setFirstname(self.firstname)
            self.addcust.setLastname(self.lastname)
            self.addcust.selectGender(self.gender)
            self.addcust.setDob("10/18/1998")
            self.addcust.setCompanyname(self.company)
            #self.addcust.setNewsletter(self.newsletter)
            self.addcust.setCustomerRole(self.role)
            self.addcust.setManagerOfVendor(self.vendor)
            self.addcust.setComment(self.comment)
            self.addcust.clickSave()


            self.logger.info("********************** Saving customer info **********************")

            self.logger.info("********************** Add customer validation started **********************")

            self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text

            print(self.msg)
            if 'customer has been added successfully.' in self.msg:
                assert True
                self.logger.info("********************* Add Customer test passed **********************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_Add_Customer.png")
                self.logger.info("********************* Add Customer test failed **********************")
                assert False

            self.addcust.clickAddnewbutton()

        self.driver.close()
        self.logger.info("*********************** add_customer Test ended ************************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
