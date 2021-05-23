import time, math, os
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

try:
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    chrome_driver_binary = "/usr/local/bin/chromedriver"
    browser = webdriver.Chrome(chrome_driver_binary, options=options)
    ans = ''
    link = 'https://stepik.org/lesson/236898/step/1'
    browser.get(link)
    browser.implicitly_wait(10)
    textera = browser.find_element_by_tag_name("textarea")
    textera.send_keys(str(math.log(int(time.time()))))
    wait = WebDriverWait(browser, 10)
    browser.implicitly_wait(5)
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    # button = browser.find_element_by_class_name("submit-submission")
    # print(button)
    button.click()
    feedback = browser.find_element_by_class_name("smart-hints__hint").text
    assert "Correct!" == feedback
finally:
    time.sleep(2)
    browser.quit()
