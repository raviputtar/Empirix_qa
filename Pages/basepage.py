from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class BasePage:

    driver=webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    driver.implicitly_wait(30)
    driver.maximize_window()

    def is_element_present(self, locator_type, locator):
        myelement = self.driver.find_element(locator_type, locator)
        if myelement is not None:
            return True
        else:
            return False

    def getelement(self, locator_type, locator):
        myelement = self.driver.find_element(locator_type, locator)
        return myelement

    def gettext(self, locator_type, locator):
        myelement = self.driver.find_element(locator_type, locator)
        mytext = myelement.text
        return mytext

    def click_element(self, locator_type, locator):
        myelement = self.driver.find_element(locator_type, locator)
        print(myelement)
        if myelement is not None:
            myelement.click()
        else:
            print("element_not_found")

    def element_sendkeys(self,data,locator_type,locator):
        myelement = self.driver.find_element(locator_type, locator)

        if myelement is not None:
            myelement.send_keys(data)
        else:
            print("element is not found")

    def title(self):
        return self.driver.title


    def wait_and_return_element(self,locator_type,locator):

        try:

            wait = WebDriverWait(self.driver, 20, poll_frequency=2,
                             ignored_exceptions=[ElementNotVisibleException, NoSuchElementException,
                                                 ElementNotSelectableException, ElementClickInterceptedException])
            element = wait.until(EC.presence_of_element_located((locator_type,locator)))
            return element
        except:
            print("page not ready")
            raise TimeoutException


