import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAccountPage:
    ##Locators
    btn_logout_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"

    ## constructor
    def __init__(self, driver):
        self.driver = driver


    ## action methods

    def clickLogout(self):
        mywait = WebDriverWait(self.driver, 10)
        time.sleep(5)
        mywait.until(EC.element_to_be_clickable((By.XPATH,self.btn_logout_xpath))).click()


