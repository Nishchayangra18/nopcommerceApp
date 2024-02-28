from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SearchCustomerPage:
    email_textbox_id = "SearchEmail"
    first_name_textbox_id = "SearchFirstName"
    last_name_textbox_id = "SearchLastName"
    Search_button_id = "search-customers"
    table_id = "customers-grid"
    Searchcustomer_table_xpath = "//div[@class='dataTables_scroll']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def Enteremail(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).clear()
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def EnterFirstname(self, firstname):
        self.driver.find_element(By.ID, self.first_name_textbox_id).clear()
        self.driver.find_element(By.ID, self.first_name_textbox_id).send_keys(firstname)

    def EnterLastname(self, lastname):
        self.driver.find_element(By.ID, self.last_name_textbox_id).clear()
        self.driver.find_element(By.ID, self.last_name_textbox_id).send_keys(lastname)

    def ClickSearchbutton(self):
        self.driver.find_element(By.XPATH, self.Search_button_id).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getNoofColums(self):
        return len(self.driver.find_elements(By.XPATH, self.table_column_xpath))

    def SearchCustomerbyEmail(self, email):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.ID, self.table_id)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomerbyName(self, Name):
        flag = False
        for r in range(1, self.getNoofRows()+1):
            table = self.driver.find_element(By.ID, self.table_id)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
