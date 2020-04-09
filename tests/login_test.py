import unittest
from Pages.loginpage import LoginPage
from Pages.homepage import HomePage

class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lp=LoginPage()
        self.lp.driver.get("https://services.empirix.com")
        self.hp=HomePage()

    def test_perform_login(self):
        self.lp.enter_username("QA_traininguser30")
        self.lp.enter_pwd("Empirix!")
        self.lp.click_signin()
        self.assertEqual("VoiceWatch", self.hp.title())

    def tearDown(self) -> None:
        pass


if __name__== "__main__":
    unittest.main()