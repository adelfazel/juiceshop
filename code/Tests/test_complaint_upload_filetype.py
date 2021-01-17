import sys
sys.path.append("..")
from ..Pages.complaint import Complaint
from .settings import browser

def test_invalid_file_type(browser):
    page = Complaint(browser)
    browser.get(page.get_url())
    page.dismiss()
    page.go_to_complaint_page()
    page.fill_message()
    page.screenshot()
    page.upload_complaint_file()
    page.submit_complaint()
    assert False, "Expecting page to reject xml file but it doesn't and submit button is active after uploading invalid file"
