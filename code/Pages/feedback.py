from selenium.common.exceptions import NoSuchElementException

from . import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Feedback(Page.Page):
    def get_url(self):
        return f"{super().get_url()}"

    def customer_feedback_element(self):
        return self.driver.find_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/sidenav/mat-nav-list/a[1]/div/span")

    def get_captcha_text(self):
        trial = 50
        while trial > 0:
            captcha = self.driver.find_element_by_id('captcha').text
            try:
                eval(captcha)
                return captcha
            except:
                sleep(0.2)
                trial -= 1
        return self.driver.find_element_by_id('captcha').text

    def feedback_set_captcha_text(self, text):
        self.driver.find_element_by_id('captchaControl').send_keys(text)

    def feedback_set_rating(self):
        move = ActionChains(self.driver)
        element = self.driver.find_element_by_xpath('//*[@id="rating"]')
        move.click_and_hold(element).move_by_offset(2, 0).release().perform()

    def feedback_set_comment_text(self, text):
        self.driver.find_element_by_xpath('//*[@id="comment"][1]').send_keys(text)

    def feedback_submit(self):
        self.driver.find_element_by_xpath('//*[@id="submitButton"]/span[1]').click()

    def feedback_change_author_id(self, authorid):
        element = self.driver.find_element_by_id('userId')
        self.driver.execute_script(f"arguments[0].value = {authorid}", element)

    def check_feedback_thankyou_is_present(self):
        try:
            self.driver.find_element_by_xpath('//*/snack-bar-container/div/div/simple-snack-bar/span')
            return True
        except NoSuchElementException:
            return False

    def fill_feedback_form(self):

        self.feedback_set_comment_text("really bad website")
        self.screenshot()
        self.feedback_set_rating()
        captcha = self.get_captcha_text()
        self.feedback_set_captcha_text(eval(captcha))

    def go_to_feedback_page(self):
        self.main_page().click()
        self.side_menu_button_element().click()
        self.customer_feedback_element().click()
