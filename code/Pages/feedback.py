from . import Page


class Feedback(Page.Page):
    def get_url(self):
        return f"{super().get_url()}/contact"

    def get_captcha_text(self):
        return self.driver.find_element_by_xpath('//*[@id="feedback-form"]/div[2]').text

    def set_captcha_text(self, text):
        self.driver.find_element_by_xpath('//*[@id="captchaControl"]').send_keys(text)
