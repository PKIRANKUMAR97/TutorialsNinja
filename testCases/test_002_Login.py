import pytest
import os
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_Login():
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()

    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self,setup):
        self.logger.info("----test_002 Testing login started----")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()
        # self.logger.info("----test_002 Testing login complete----")

        self.lp=LoginPage(self.driver)
        self.lp.enter_email(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else :
            screenshotpath=os.path.join(os.getcwd(),"screenshots","test_002_Login_failure.png")
            self.driver.save_screenshot(screenshotpath)
            assert False

        self.driver.close()
        self.logger.info("----test_002 Testing login complete----")