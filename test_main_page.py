from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

base_link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    login_page = LoginPage(browser, link)
    login_page.open()                      # открываем страницу
    login_page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    cart_page = CartPage(browser, base_link)
    cart_page.open()
    cart_page.go_to_cart_page()
    cart_page.should_be_empty_cart()
