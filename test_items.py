import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button_should_be_on_page(browser):
    browser.get(link)
    add_btn_list = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    print("Number of returned buttons: {}".format(len(add_btn_list)))
    assert len(add_btn_list) == 1, "Expected 1 returned button, instead of {}".format(len(add_btn_list))
