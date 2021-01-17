import random
import string

class Page:
    def __init__(self, driver):
        import os
        self.url = os.environ.get("host", "http://localhost:3000/")

        driver.maximize_window()
        self.driver = driver

    def get_url(self):
        return self.url

    def go_to_base_url(self):
        self.driver.get(self.get_url())

    def get_title(self):
        return self.driver.title

    def side_menu_button_element(self):
        return self.driver.find_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[1]/span[1]/mat-icon")

    def main_page(self):
        return self.driver.find_element_by_xpath(
            '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[2]/span[1]/span')

    def screenshot(self, base=None):
        def create_file_name(index):
            if base:
                return f"{directory}/{base}_{index}.png"
            return f"{directory}/{index}.png"

        import os
        directory = "artefacts"
        filename = create_file_name(1)
        if not os.path.exists(filename):
            self.driver.save_screenshot(filename)
            return
        else:
            lastfile = 2
            filename = create_file_name(lastfile)
            while os.path.exists(filename):
                lastfile += 1
                filename = create_file_name(lastfile)
            self.driver.save_screenshot(filename)
            return

    def scroll_down(self):
        pass

    def dismiss(self):
        try:
            element = self.driver.find_element_by_xpath(
                '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
            self.driver.execute_script("arguments[0].click();", element)
        except:
            pass


    def login(self, username='studentm_ele@yahoo.com', password='aassddaa'):
        self.driver.find_element_by_id('navbarAccount').click()
        self.driver.find_element_by_id('navbarLoginButton').click()
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('loginButton').click()
