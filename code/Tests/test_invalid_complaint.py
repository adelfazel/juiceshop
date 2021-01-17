from ..Pages.complaint import Complaint
from .settings import browser
import os


def test_invalid_file_type(browser):
    page = Complaint(browser)
    page.go_to_base_url()
    page.dismiss()
    page.login()
    page.screenshot()
    page.go_to_complaint_page()


    page.fill_message()
    print(os.getcwd())
    page.upload_complaint_file()
    page.screenshot()


# def test_invalid_file_type(browser):
#     page = Complaint(browser)
#     page.login()
#     page.go_to_complaint_page()
#     page.fill_message()
#     page.upload_complaint_file("tictactoe.zip")
#     page.screenshot()
