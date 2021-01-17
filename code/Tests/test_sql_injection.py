from ..Pages.mainpage import Mainpage

from .settings import browser
def test_login_injection_bender(browser):
    page = Mainpage(browser)
    browser.get(page.get_url())
    page.dismiss()
    page.login("bender@juice-sh.op'--", "asdsa")
    page.screenshot("test_login_injection_bender")
    assert not page.invalid_login_message_is_present(), "was able to login without password"
