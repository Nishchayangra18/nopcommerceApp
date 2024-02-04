import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class CustomerPage:
    customer_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    customer_menuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(), 'Customers')]"
    addNew_button_xpath = "//a[@class='btn btn-primary']"
    # customerInfo_xpath = "//div[@class='card-header with-border clearfix']"
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    firstName_textbox_id = "FirstName"
    lastName_textbox_id = "LastName"
    gender_male_radioButton_id = "Gender_Male"
    gender_female_radioButton_xpath = "Gender_Female"
    dob_id = "DateOfBirth"
    companyName_textbox_id = "Company"
    taxExempt_checkBox_id = "IsTaxExempt"
    newsLetter_textbox_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    customerRoles_textbox_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    list_customerRoles_Registered_xpath = "//li[contains(text(), 'Registered')]"
    list_customerRoles_Vendors_xpath = "//li[contains(text(), 'Vendors')]"
    list_customerRoles_Guests_xpath = "//li[contains(text(), 'Guests')]"
    list_customerRoles_ForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    list_customerRoles_Administrators_xpath = "//li[contains(text(), 'Administrators')]"
    managerofVendor_textbox_id = "VendorId"
    active_checkBox_id = "Active"
    adminComment_textbox_id = "AdminComment"
    save_button_xpath = "//button[@name='save']"
    # list_newsletter_yourstorename_xpath = "//span[contains(text(), 'Your store name')]"
    # list_newsletter_teststore_2_xpath = "//span[contains(text(), 'Test store 2')]"

    def __init__(self, driver):
        self.driver = driver

    def ClickCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.customer_menu_xpath).click()
        time.sleep(3)

    def ClickCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.customer_menuItem_xpath).click()
        time.sleep(5)

    def clickAddnewbutton(self):
        self.driver.find_element(By.XPATH, self.addNew_button_xpath).click()
        time.sleep(5)

    # def clickCustomerinfo(self):
    #     self.driver.find_element(By.XPATH, self.customerInfo_xpath).click()

    def Setemail(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).clear()
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.ID, self.firstName_textbox_id).clear()
        self.driver.find_element(By.ID, self.firstName_textbox_id).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.ID, self.lastName_textbox_id).clear()
        self.driver.find_element(By.ID, self.lastName_textbox_id).send_keys(lastname)

    def selectGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.gender_male_radioButton_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.gender_female_radioButton_xpath).click()
        else:
            self.driver.find_element(By.ID, self.gender_male_radioButton_id).click()

    def setDob(self, dob):
        self.driver.find_element(By.ID, self.dob_id).clear()
        self.driver.find_element(By.ID, self.dob_id).send_keys(dob)

    def setCompanyname(self, company):
        self.driver.find_element(By.ID, self.companyName_textbox_id).clear()
        self.driver.find_element(By.ID, self.companyName_textbox_id).send_keys(company)

    def selecttaxExempt(self):
        self.driver.find_element(By.ID, self.taxExempt_checkBox_id).click()

    # def setNewsletter(self, newsletter):
    #     self.driver.find_element(By.XPATH, self.newsLetter_textbox_xpath).click()
    #     time.sleep(3)
    #     if newsletter == "Your store name":
    #         actions = webdriver.ActionChains(self.driver)
    #         actions.send_keys(Keys.ENTER)
    #     elif newsletter == "Test store 2":
    #         actions = webdriver.ActionChains(self.driver)
    #         actions.send_keys(Keys.ARROW_DOWN)
    #         actions.send_keys(Keys.ENTER)
    #     else:
    #         actions = webdriver.ActionChains(self.driver)
    #         actions.send_keys(Keys.ARROW_DOWN)
    #         actions.send_keys(Keys.ENTER)

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.customerRoles_textbox_xpath).click()
        time.sleep(3)
        if role == "Registered":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRoles_Registered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRoles_Vendors_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRoles_ForumModerators_xpath)

            # Here user can be Registered or Guests, only one

        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRoles_Guests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRoles_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRoles_Administrators_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_customerRoles_Registered_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, vendor):
        drp = Select(self.driver.find_element(By.ID, self.managerofVendor_textbox_id))
        drp.select_by_visible_text(vendor)

    def clickActive(self):
        self.driver.find_element(By.ID, self.active_checkBox_id).click()

    def setComment(self, comment):
        self.driver.find_element(By.ID, self.adminComment_textbox_id).clear()
        self.driver.find_element(By.ID, self.adminComment_textbox_id).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
        time.sleep(5)
