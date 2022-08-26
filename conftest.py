import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default=None, help="Choose browser: Chrome or "
                                                                                         "Firefox")
    parser.addoption('--languages', action='store', default=None,
                     help="Choose language: ec or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('languages')
    browser = None
    if browser_name == "chrome":
        print("\nStrart Chrome browser for test.. ")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nStrart Firefox browser for test.. ")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nBrowser quit..")
    browser.quit()