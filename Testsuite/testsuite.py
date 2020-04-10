import unittest
import HtmlTestRunner

from tests.login_test import LoginTest
from tests.hometest import HomeTest
from tests.Japanese_test import JapaneseTest


class TestSuite(unittest.TestSuite):
    tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    tc2=unittest.TestLoader().loadTestsFromTestCase(HomeTest)
    tc3=unittest.TestLoader().loadTestsFromTestCase(JapaneseTest)


    def test_run_suite(self):
        my_suite=unittest.TestSuite([self.tc1,self.tc2,self.tc3])
        unittest.TextTestRunner(verbosity=2).run(my_suite)


if __name__== "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))