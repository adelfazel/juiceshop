import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    try:
        driver = webdriver.Chrome(options=get_chrome_options())
        yield driver
        driver.close()
        driver.quit()
    except Exception as e:
        print(f"Unable to instanciate browser, most likely due to problem with error:{e}, ensure docker settings are OK!")

def get_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.experimental_options["prefs"] = {}
    return chrome_options