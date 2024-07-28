import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class searchPage():
    def __init__(self, driver):
        self.driver = driver
        self.search_id = "gh-ac"
        self.title_css = "div[class='s-item__title']"
        self.button_sorting_css ="button[class='fake-menu-button__button btn btn--small btn--secondary']"
        self.free_shipping_css ="span[class='s-item__shipping s-item__logisticsCost']"

    def searchItem(self, item):
        search = self.driver.find_element(By.ID,self.search_id)
        search.click()
        search.clear()
        search.send_keys(item)
        print(f'searching for {item}')
        search.send_keys(Keys.ENTER)

    def find_key_word(self, item_to_find,check_num):
        titles = self.driver.find_elements(By.CSS_SELECTOR, self.title_css)
# start loop
        total_num = 0
        for title in titles:
            is_in_text = title.text.count(item_to_find)
            total_num = total_num + is_in_text
# stop loop
        print (f'number times found GPS {total_num}')
        assert total_num > check_num, "GPS not found in title"


    def sorting(self):
        button_sorting = self.driver.find_elements(By.CSS_SELECTOR, self.button_sorting_css)
        button_sorting[2].click()
        check_boxes_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Free International Shipping")
        check_boxes_link.click()
        time.sleep(3)

    def check_sorting(self):
        free_shipping = self.driver.find_element(By.CSS_SELECTOR,self.free_shipping_css)
        text_free_shipping = free_shipping.text
        print(f'shipping cost {text_free_shipping}')
        return text_free_shipping
