from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class CatalogueLocators():
    ITEM_URL = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADD_BUTTON = (By.CSS_SELECTOR, '.add-to-basket')
    ITEM_CART_NAME = (By.CSS_SELECTOR, '.alertinner')
    ITEM_CART_PRICE = (By.CSS_SELECTOR, '.alert:nth-child(3) .alertinner p')
