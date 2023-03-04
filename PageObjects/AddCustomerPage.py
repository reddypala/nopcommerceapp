import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class AddCustomer():
    # Add customer elements
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lknCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtCustomerRoles_xpath = "(//input[@role='listbox'])[2]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='guests']"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_id = "VendorId"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtComapanyName_xpath = "//input[@id='Company']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lknCustomers_menuitem_xpath).click()

    def clcikOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(pwd)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        if role == 'Registered':
            self.listItem = self.driver.find_element(By.XPATH,
                                                     "//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='" + role + "']")
        elif role == 'Administrators':
            self.listItem = self.driver.find_element(By.XPATH,
                                                     "//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='" + role + "']")
        elif role == 'Guests':
            # Here user can be Registered or Guest, only one
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            time.sleep(3)
            try:
                self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
            except:
                self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
                self.listItem = self.driver.find_element(By.XPATH,
                                                         "//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='" + role + "']")
        elif role == 'Vendors':
            self.listItem = self.driver.find_element(By.XPATH,
                                                     "//ul[@id='SelectedCustomerRoleIds_listbox']/li[text()='" + role + "']")
        else:
            self.driver.find_element(By.XPATH, self.lstitemGuests_xpath).click()
        time.sleep(3)
        self.listItem.click()
        # self.driver.execute_script("arguments[0].click()",self.listItem)

    def setManagerVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.drpmgrOfVendor_id))
        drp.select_by_visible_text(value)

    def selectGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDOB(self, date):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(date)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txtComapanyName_xpath).send_keys(companyName)

    def clickSaveBtn(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
