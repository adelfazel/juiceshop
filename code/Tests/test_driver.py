from .settings import browser

def test_driver(browser):
    browser.get("https://www.google.com")
    assert 'google' in (browser.title).lower(), f"Expecting google website contains \
                                            'google' in title but it doesn't. \
                                            Instead it is:{browser.title}"
