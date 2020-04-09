from Pages.basepage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):


    alerts_link='Alerts'
    tests_link='Tests'
    variables_link = 'Variables'
    notify_link='Notifications'
    dashboard_link='Dashboard'

    def click_dashboard(self):
        self.click_element(By.LINK_TEXT,self.dashboard_link)

    def click_tests(self):
        self.click_element(By.LINK_TEXT,self.tests_link)

    def click_variables(self):
        self.click_element(By.LINK_TEXT,self.variables_link)

    def click_notify(self):
        self.click_element(By.LINK_TEXT,self.notify_link)

    def click_alerts(self):
        self.click_element(By.LINK_TEXT,self.alerts_link)

