from korzina_stepik.pages.product_page import ProductPage
import time
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(3)
    page.press_button_cart()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_message_about_adding()
    time.sleep(3)
    page.should_be_message_basket_total()
