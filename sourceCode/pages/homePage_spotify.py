class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.homepage_login_xpath = "//*[@id='main']/div/div[2]/div[1]/header/div[5]/button[2]"

    def click_homepage_login(self):
        self.driver.find_element_by_xpath(self.homepage_login_xpath).click()

