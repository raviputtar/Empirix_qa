import unittest
import HtmlTestRunner
from Pages.loginpage import LoginPage
from Pages.homepage import HomePage
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.lp=LoginPage()
        cls.lp.driver.get("https://services.empirix.com")
        cls.hp=HomePage()

    def test_perform_login(self):
        self.lp.enter_username("QA_traininguser30")
        self.lp.enter_pwd("Empirix!")
        self.lp.click_signin()

    def test_title_after_login(self):
        myelement = self.lp.wait_and_return_element(By.XPATH, self.hp.training_xpath)
        if myelement is not None:
            self.assertEqual("VoiceWatch", self.hp.title())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.lp.driver.close()


if __name__== "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))