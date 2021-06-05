from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_have_button_basket(browser):
    browser.get(link)
    q = len(browser.find_elements_by_css_selector("button.btn-primary"))
    assert q > 0, 'Элемент не найден!'



