import unittest
import time
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        try:
            SEARCH_WORD = 'python'
            self.browser.get('http://www.google.com')
            self.assertIn('Google', self.browser.title)
        finally:
            self.browser.quit()

    def testSearchTitle(self):
        try:
            SEARCH_WORD = 'python'
            self.browser.get('http://www.google.com')
            time.sleep(3)
            search_input = self.browser.find_element_by_name('q')
            search_input.send_keys(SEARCH_WORD)
            search_input.submit()
            time.sleep(3)
            self.assertIn(SEARCH_WORD + ' - Google 検索', self.browser.title)
        finally:
            self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

