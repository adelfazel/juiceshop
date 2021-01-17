import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_browser():
    driver = webdriver.Chrome(options=get_chrome_options())
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_window_size(1920, 1080)
    return driver

@pytest.fixture()
def browser():
    try:
        driver = webdriver.Chrome(options=get_chrome_options())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.set_window_size(1920, 1080)
        yield driver
        driver.close()
        driver.quit()
    except Exception as e:
        print(
            f"Unable to instanciate browser, most likely due to problem with error:{e}, ensure docker settings are OK!")


def get_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024,800")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.experimental_options["prefs"] = {}
    return chrome_options
