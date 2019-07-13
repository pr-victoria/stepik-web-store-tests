import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_should_be_on_page(browser):
    browser.get(link)
    browser.wait = WebDriverWait(browser, 5)
    add_btn_list = browser.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    print("Number of returned buttons: {}".format(len(add_btn_list)))
    time.sleep(5)
    assert len(add_btn_list) == 1, "Expected 1 returned button, instead of {}".format(len(add_btn_list))
