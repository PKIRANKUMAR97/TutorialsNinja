from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    #Locators
    txt_firstname_NAME="firstname"
    txt_lastname_NAME="lastname"
    txt_email_NAME="email"
    txt_telephone_NAME="telephone"
    txt_password_NAME="password"
    txt_confpassword_NAME="confirm"
    chk_policy_NAME="agree"
    btn_continue_XPATH="//input[@value='Continue']"
    text_msg_conf_XPATH="//h1[normalize-space()='Your Account Has Been Created!']"

    #Constructor
    def __init__(self, driver):
        self.driver = driver

    #Action Methods
    def setFirstname(self,firstname):
        self.driver.find_element(By.NAME,self.txt_firstname_NAME).send_keys(firstname)
    def setLastname(self,lastname):
        self.driver.find_element(By.NAME,self.txt_lastname_NAME).send_keys(lastname)
    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_NAME).send_keys(email)
    def setTelephone(self,telephone):
        self.driver.find_element(By.NAME,self.txt_telephone_NAME).send_keys(telephone)
    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.txt_password_NAME).send_keys(password)
    def setConfirmPassword(self,cnfpwd):
        self.driver.find_element(By.NAME,self.txt_confpassword_NAME).send_keys(cnfpwd)
    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME,self.chk_policy_NAME).click()
    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_continue_XPATH).click()
    def getconfirmationmessage(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_conf_XPATH).text
        except:
            None
