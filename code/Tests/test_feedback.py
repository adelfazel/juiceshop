import sys

sys.path.append("..")
from ..Pages import mainpage
from .settings import browser


def test_feedback(browser):
    page = mainpage.Mainpage(browser)
    browser.get(page.get_url())
    assert "OWASP" in page.get_title(), f"invalid page title: {page.get_title()}"
    page.dismiss()
    page.go_to_feedback()
    assert set("-+*/").intersection(
        set(page.get_captcha_text())), f"captcha contains no arithamtic expression {page.get_captcha_text()}"
    page.feedback_set_captcha_text(eval(page.get_captcha_text()))
    page.screenshot()
    page.feedback_set_author_text("Tester")
    page.feedback_set_comment_text("really bad website")
    page.screenshot()
    page.feedback_submit()
    page.screenshot()
