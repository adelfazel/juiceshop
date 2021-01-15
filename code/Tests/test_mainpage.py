import sys
sys.path.append("..")
from ..Pages import mainpage
from .settings import browser

def test_feedback(browser):
    page = mainpage.Mainpage(browser)
    browser.get(page.get_url())
    page.side_menu_button().click()
    page.customer_feedback().click()
    assert page.title.lower() in "OWASP",page.title
