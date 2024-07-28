from selenium.webdriver.common.by import By


class productPage():
    def __init__(self, driver):
        self.driver = driver
        self.price_css="span[class='ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD']"

    def check_product_price(self):
        price = self.driver.find_element(By.CSS_SELECTOR,self.price_css)
        price_text = price.text
        slice_string_end = price_text[4:]
        print(f'price found {slice_string_end}')
        return slice_string_end
