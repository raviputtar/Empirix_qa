from Pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):


    alerts_xpath='//a[@href="/alerts"]'
    tests_xpath='//a[@href="/tests"]'
    variables_xpath = '//a[@href="/variables"]'
    notify_xpath='//a[@href="/notify"]'
    dashboard_xpath='//a[@href="/dashboard"]'

    def click_dashboard(self):
        self.click_element(By.XPATH,self.dashboard_xpath)

    def click_tests(self):
        self.click_element(By.XPATH,self.tests_xpath)

    def click_variables(self):
        self.click_element(By.XPATH,self.variables_xpath)

    def click_notify(self):
        self.click_element(By.XPATH,self.notify_xpath)

    def click_alerts(self):
        self.click_element(By.XPATH,self.alerts_xpath)