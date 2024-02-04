import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, Setup):

        self.logger.info("********************** Test_001_Login ************************")
        self.logger.info("********************** Verifying Home Page Title  ************************")
        self.driver = Setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********************** Home Page Title test case is passed ************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********************** Home Page Title test case is failed ************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, Setup):

        self.logger.info("********************** Verifying Log in  ************************")
        self.driver = Setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********************** Login Test case passed  ************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("********************** Login Test case failed  ************************")
            self.driver.close()
            assert False
