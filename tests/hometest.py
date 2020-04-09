import unittest
from Pages.loginpage import LoginPage
from Pages.homepage import HomePage

class HomeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lp=LoginPage()
        self.lp.driver.get("https://services.empirix.com")
        self.hp=HomePage()
        self.lp.enter_username("QA_traininguser30")
        self.lp.enter_pwd("Empirix!")
        self.lp.click_signin()

    def test_all_links(self):
        self.hp.click_alerts()
        self.hp.click_dashboard()
        self.hp.click_notify()
        self.hp.click_tests()
        self.hp.click_variables()


    def tearDown(self) -> None:
        self.hp.driver.quit()


if __name__== "__main__":
    unittest.main()