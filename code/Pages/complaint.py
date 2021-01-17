from . import Page
import os
from time import sleep


class Complaint(Page.Page):
    def get_url(self):
        return f"{super().get_url()}"

    def get_compliant_sidebar_element(self):
        return self.driver.find_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/sidenav/mat-nav-list/a[2]")

    def get_compliant_message_element(self):
        return self.driver.find_element_by_xpath(
            '//*[@id="complaintMessage"]')

    def go_to_complaint_page(self):
        self.main_page().click()
        self.side_menu_button_element().click()
        self.get_compliant_sidebar_element().click()

    def fill_message(self, message="SSSDDWQWQE"):
        self.get_compliant_message_element().send_keys(message)

    def upload_complaint_file(self, filename='invalidtype'):
        self.driver.find_element_by_id('file').send_keys(f"{os.getcwd()}/files/{filename}")
