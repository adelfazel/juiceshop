from . import Page


class Mainpage(Page.Page):
    def get_url(self):
        return f"{super().get_url()}"

    def side_menu_button(self):
        return self.driver.find_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[1]/span[1]/mat-icon")

    def customer_feedback(self):
        return self.driver.find_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/sidenav/mat-nav-list/a[1]/div/span")

    def main_page(self):
        return self.driver.find_element_by_xpath(
            '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[2]/span[1]/span')

    def get_captcha_text(self):
        return self.driver.find_element_by_xpath('//*[@id="captcha"]').text

    def feedback_set_captcha_text(self, text):
        self.driver.find_element_by_xpath('//*[@id="captchaControl"]').send_keys(text)

    def feedback_set_author_text(self, text):
        self.driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(text)

    def feedback_set_comment_text(self, text):
        self.driver.find_element_by_xpath('//*[@id="comment"]').send_keys(text)

    def feedback_submit(self):
        self.driver.find_element_by_xpath('//*[@id="submitButton"]/span[1]').click()

    def go_to_feedback(self):
        self.main_page().click()
        self.side_menu_button().click()
        self.customer_feedback().click()
