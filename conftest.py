from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or es")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language == "ru":
        print("\nstart RU LANGUAGE browser for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "es":
        print("\nstart ES LANGUAGE browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or es")
    yield browser
    print("\nquit browser..")
    browser.quit()






# link = "http://selenium1py.pythonanywhere.com/"
#
#
# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")

