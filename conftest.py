import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or es or fr")


@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    browser = webdriver.Chrome()
    if language_name == "es":
        link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
        browser.get(link)
    elif language_name == "fr":
        link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
        browser.get(link)
    elif language_name == "ru":
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        browser.get(link)
    yield browser
    browser.quit()
