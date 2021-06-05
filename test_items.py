from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_have_button_basket(browser):
    browser.get(link)
    try:
        browser.find_element_by_css_selector("[value='Добавить в корзину']")
    except NoSuchElementException as error:
        return error
    return print('Элемент найден!')


