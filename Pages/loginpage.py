from Pages.basepage import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    #locators
    username_locator="callback_0"
    pwd_locator="callback_1"
    signin_locator="callback_2"

    def enter_username(self,username):
        self.element_sendkeys(username,By.NAME,self.username_locator)

    def enter_pwd(self,pwd):
        self.element_sendkeys(pwd,By.NAME,self.pwd_locator)

    def click_signin(self):
        self.click_element(By.NAME,self.signin_locator)

    def do_login(self,username,pwd):
        self.enter_username(username)
        self.enter_pwd(pwd)
        self.click_signin()



