from selenium import webdriver

class basepage:

    driver=webdriver.Chrome(executable_path="")

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
