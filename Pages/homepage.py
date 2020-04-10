from Pages.basepage import BasePage
from selenium.webdriver.common.by import By



class HomePage(BasePage):


    #locators

    alerts_link='Alerts'
    tests_link='Tests'
    variables_link = 'Variables'
    notify_link='Notifications'
    dashboard_link='Dashboard'
    training_xpath='//a[@class="dropdown-toggle ng-binding"]'
    japanese_language_xpath='//a[@style=" display:inline"]'
    english_language_xpath='//a[@style=" display:inline"]'


    #japanese_language_xpath = '//a[@style=" display:inline"]'
    #english_language_xpath = '//a[@style=" display:inline"]'

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

    def click_japanese(self):

        training_element=self.wait_and_return_element(By.XPATH,self.training_xpath)
        training_element.click()

        japanese_element = self.wait_and_return_element(By.XPATH, self.japanese_language_xpath)
        self.driver.execute_script("arguments[0].click();", japanese_element)

    def handle_alert(self):
        alert=self.driver._switch_to.alert
        alert.accept()

    def click_english(self):
        training_element = self.wait_and_return_element(By.XPATH, self.training_xpath)
        training_element.click()

        english_element = self.wait_and_return_element(By.XPATH, self.english_language_xpath)
        self.driver.execute_script("arguments[0].click();", english_element)









