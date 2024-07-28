import time
import unittest

from selenium.webdriver.common.by import By

from projectEbay.pages.productPage import productPage
from projectEbay.pages.searchPage import searchPage
from projectEbay.tests.baseProjectSelenium import baseProjectSelenium
from projectEbay.tests.globals import url, searchTerm, key_word, ref


class test_allTests(unittest.TestCase):
    def setUp(self):
        self.base = baseProjectSelenium()
        self.driver = self.base.selenium_start(url)
        self.search_page = searchPage(self.driver)

    def test_KeyWord(self):
        self.search_page.searchItem(searchTerm)
        time.sleep(3)
        self.search_page.find_key_word(key_word,ref)


    def test_sorting(self):
        self.search_page.searchItem(searchTerm)
        time.sleep(3)
        self.search_page.sorting()
        text_to_check = self.search_page.check_sorting()
        assert text_to_check == "Free International Shipping", "not showing - Free International Shipping"


    def test_priceProduct(self):
        product_page = productPage(self.driver)
        self.search_page.searchItem(searchTerm)
        time.sleep(3)

        product_link = self.driver.find_element(By.PARTIAL_LINK_TEXT,"New GPS Smart Watch Men Pro HD Screen")
        url_page_product = product_link.get_attribute("href")
        product_link.click()
        self.driver.get(url_page_product)

        price_watch = product_page.check_product_price()
        assert  price_watch == "292.20", "not the right price"


    def tearDown(self):
        self.base.selenium_end(self.driver)

