from .base_page import BasePage
from .locators import CatalogueLocators

class ProductPage(BasePage):
    def cart_info_should_be_correct(self):
        self.item_name_correct()
        self.item_price_correct()

    def item_name_correct(self):
        itemcartname = self.browser.find_element(*CatalogueLocators.ITEM_CART_NAME)
        itemname = self.browser.find_element(*CatalogueLocators.ITEM_NAME)
        text_itemcartname = itemcartname.text
        text_itemname = itemname.text
        assert text_itemcartname[:len(text_itemname)] == text_itemname, \
            f"Expected item name is '{text_itemname}', but was '{text_itemcartname[:len(text_itemname)]}'"
        assert True

    def item_price_correct(self):
        itemcartprice = self.browser.find_element(*CatalogueLocators.ITEM_CART_PRICE)
        itemprice = self.browser.find_element(*CatalogueLocators.ITEM_PRICE)
        text_itemcartprice = itemcartprice.text
        text_itemprice = itemprice.text
        assert text_itemcartprice[-len(text_itemprice):] == text_itemprice, \
            f"Expected item name is '{text_itemprice}', but was '{text_itemcartprice[-len(text_itemprice):]}'"
        assert True

    def add_to_cart(self):
        link = self.browser.find_element(*CatalogueLocators.ADD_BUTTON)
        link.click()