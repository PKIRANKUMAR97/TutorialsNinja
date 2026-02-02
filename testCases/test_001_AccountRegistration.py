import os.path
import time

from pageObjects import HomePage, AccountRegistrationPage
from utilities import randomString


# from pageObjects.FileName import ClassName
# from pageObjects.HomePage import HomePage


class Test_001_AccountReg:
    base_url="https://tutorialsninja.com/demo/"

    def test_account_registration(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp = HomePage.HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage=AccountRegistrationPage.AccountRegistrationPage(self.driver)
        self.regpage.setFirstname("Johnn")
        self.regpage.setLastname("Kinder")
        # self.regpage.setEmail("qxxdrfftt1@gmail.com")
        # self.regpage.setEmail=randomString.random_string_generator()+'@gmail.com'
        self.regpage.setTelephone("55555589")
        self.regpage.setPassword("johnqwer@")
        self.regpage.setConfirmPassword("johnqwer@")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        # time.sleep(5)
        self.confmsg=self.regpage.getconfirmationmessage()
        # time.sleep(5)
        # self.driver.close()
        if self.confmsg=="Your Account Has Been Created!":

            assert True
            self.driver.close()
        else:
            # self.driver.save_screenshot(os.path.abspath(os.curdir))+"\\screenshots\\"+"test_account_reg.png"
            screenshot_path = os.path.join(os.path.abspath(os.curdir), "screenshots", "test_account_reg.png")
            self.driver.save_screenshot(screenshot_path)
            assert False
            self.driver.close()



