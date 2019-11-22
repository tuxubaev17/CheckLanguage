import pytest
import time

def test_check_basket_with_other_language(browser):
    time.sleep(30)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    l = len(button)
    assert l > 0, "Missing element on page"
