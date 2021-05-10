import time, math, os
from selenium import webdriver
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary, options=options)
wait = WebDriverWait(browser, 10)
# with open("test.txt", "w") as file:
#     content = file.write("automationbypython")
# def get_twits ():

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    print(wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")))
    button = browser.find_element_by_id("book")
    button.click()
    # confirm = browser.switch_to.alert
    # confirm_text = confirm.text
    # confirm.accept()
    # print(confirm_text)
    browser.execute_script("window.scrollTo(0,100)")

    # new_window = browser.window_handles[1]
    # print(browser.window_handles)
    # browser.switch_to.window(new_window )
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    val = browser.find_element_by_id('input_value').text
    print(val)
    ans = calc(val)
    print(calc(val))
    inp = browser.find_element_by_id('answer')
    inp.send_keys(ans)
    button = browser.find_element_by_id("solve")
    button.click()
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)
    pyperclip.copy(answer)
    alert.accept()
finally:
    time.sleep(10)
    browser.quit()