import time
import unittest
from selenium import webdriver

class SearchFunctionaltyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\selenium-python\\driver\\chromedriver.exe")

    def test_search_functionality(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/")
        time.sleep(5)

        searched_word = "interview questions"

        search_field = driver.find_element_by_name("search_block_form")
        search_button = driver.find_element_by_class_name("icon.glyphicon.glyphicon-search")

        search_field.send_keys(searched_word)
        search_button.click()
        time.sleep(2)

        search_results = driver.find_elements_by_css_selector(".title a")

        for result in search_results:
            self.assertIn(searched_word, result.text.lower())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
