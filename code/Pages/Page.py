class Page:
    def __init__(self, driver):
        import os
        self.url = os.environ.get("host", "http://localhost:3000/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        self.driver = driver

    def get_url(self):
        return self.url

    def get_title(self):
        return self.driver.title

    def screenshot(self):
        import os
        directory = "artefacts"
        filename = f"{directory}/1.png"
        if not os.path.exists(filename):
            self.driver.save_screenshot(filename)
            return
        else:
            lastfile = 2
            filename = f"{directory}/{lastfile}.png"
            while os.path.exists(filename):
                lastfile += 1
                filename = f"{directory}/{lastfile}.png"
            self.driver.save_screenshot(filename)
            return

    def dismiss(self):
        try:
            element = self.driver.find_element_by_xpath(
                '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
            self.driver.execute_script("arguments[0].click();", element)
        except:
            pass
