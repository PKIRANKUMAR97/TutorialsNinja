import os
import time
from os import getcwd

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import XLUtils
from pageObjects.HomePage import  HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage


class Test_003_Login_DataDriven():
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    path = os.path.join(getcwd(),"testData","TutorialsNinja_LoginData.xlsx")

    def test_login_DataDriven(self, setup):
        self.logger.info("******  starting test_003_login_DataDriven   *******")
        self.noofrows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        # self.map= MyAccountPage(self.driver)

        for r in range(2,self.noofrows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()
            self.map = MyAccountPage(self.driver)
            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.pwd = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.enter_email(self.email)
            self.lp.enter_password(self.pwd)
            self.lp.click_login()
            time.sleep(2)

            self.targetpage=self.lp.isMyAccountPageExists()
            if self.exp =='Valid':
                if self.targetpage==True:
                    lst_status.append("Pass")
                    self.hp.clickMyAccount()
                    self.map.clickLogout()
                else:
                    lst_status.append("Fail")

            else:
                if self.exp=="Invalid":
                    if self.targetpage==True:
                        lst_status.append("Fail")
                        self.hp.clickMyAccount()
                        self.map.clickLogout()
                    else :
                        lst_status.append("Pass")



        if "Fail" in lst_status:
            assert False
        else:
            assert True

        self.logger.info("******  finished test_003_login_DataDriven   *******")





