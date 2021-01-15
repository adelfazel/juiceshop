class Mainpage:
    def __init__(self, driver):
        import os
        self.url = os.environ.get("host", "http://localhost:3000/")
        self.driver = driver

    def get_url(self):
        return self.url

    def side_menu_button(self):
        return self.driver.get_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[1]/span[1]/mat-icon")

    def customer_feedback(self):
        return self.driver.get_element_by_xpath(
            "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/sidenav/mat-nav-list/a[1]/div/span")
