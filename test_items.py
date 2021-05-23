import time, math, os
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


class Test_items():
    def test_stepik_link(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(5)
        browser.implicitly_wait(3)
        button = browser.find_element_by_class_name("btn-add-to-basket")
        assert button, 'Basket button not found!'


if __name__ == "__main__":
    pytest.main()
