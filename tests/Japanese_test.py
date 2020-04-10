import unittest
from Pages.loginpage import LoginPage
from Pages.homepage import HomePage


class JapaneseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.lp = LoginPage()
        cls.lp.driver.get("https://services.empirix.com")
        cls.hp = HomePage()
        cls.lp.enter_username("QA_traininguser30")
        cls.lp.enter_pwd("Empirix!")
        cls.lp.click_signin()


    def test_switch_to_japanese(self):
        self.hp.click_japanese()
        self.hp.handle_alert()

    def test_switch_to_english(self):
        self.hp.click_english()
        self.hp.handle_alert()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.lp.driver.quit()


if __name__ == "__main__":
    unittest.main()