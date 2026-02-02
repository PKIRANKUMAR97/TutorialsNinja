from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage():
    #Locators
    lnk_myaccount_xpath="//span[normalize-space()='My Account']"
    lnk_register_linktext="Register"
    lnk_login_linktext="Login"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    #Action Methods

    def clickMyAccount(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_myaccount_xpath))
        ).click()

    def clickRegister(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.lnk_register_linktext))).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()
