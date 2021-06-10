from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from korzina_stepik.pages.product_page import ProductPage
import math

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()


