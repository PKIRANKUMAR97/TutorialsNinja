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
        # self.regpage.setEmail("qxxdrfftt88@gmail.com")
        self.email=randomString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
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

        else:
            screenshot_path = os.path.join(os.getcwd(), "screenshots", "test_account_reg_failure.png")

            self.driver.save_screenshot(screenshot_path)
            assert False






