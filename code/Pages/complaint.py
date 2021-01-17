from . import Page
import os


class Complaint(Page.Page):
    def get_url(self):
        return f"{super().get_url()}"

    def get_compliant_sidebar_element(self):
        return self.driver.find_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/sidenav/mat-nav-list/a[2]")

    def get_compliant_message_element(self):
        return self.driver.find_element_by_xpath(
            '//*[@id="complaintMessage"]')

    def get_complaint_url(self):
        return f"{self.get_url()}/#/complain"

    def go_to_complaint_page(self):
        self.driver.get(self.get_complaint_url())

    def fill_message(self, message="SSSDDWQWQE"):
        self.get_compliant_message_element().send_keys(message)

    def submit_complaint(self):
        self.driver.find_element_by_id("submitButton").click()

    def upload_complaint_file(self, filename='invalidtype.xml'):
        fullpath = f"{os.getcwd()}/files/{filename}"
        self.driver.find_element_by_id('file').send_keys(fullpath)
