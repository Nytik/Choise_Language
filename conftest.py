from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or es")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    for i in browser.find_elements_by_css_selector('select option'):
        z = z + ' ' + i.get_attribute('value')
    if language in z:
        print(f"\nstart {language} LANGUAGE browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError(f"--language should be in {z}")
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()


