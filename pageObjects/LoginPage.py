import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    ##Locators
    txt_email_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//input[@type='submit']"
    txt_MYACCOUNT_xpath = "//h2[text()='My Account']"


    ## constructor
    def __init__(self, driver):
        self.driver = driver

    ##Action methods
    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def isMyAccountPageExists(self):
        try:
            mywait = WebDriverWait(self.driver, 10)
            element_MYACCOUNT =mywait.until(EC.visibility_of_element_located((By.XPATH,self.txt_MYACCOUNT_xpath)))
            return element_MYACCOUNT.is_displayed()

        except:
            return False


