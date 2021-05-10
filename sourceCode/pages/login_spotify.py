class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.login_button_xpath = "//*[@id='main']/div/div[2]/div[1]/header/div[5]/button[2]"
        self.login_username_id = "login-username"
        self.login_password_id = "login-password"
        self.login_button_id = "login-button"

    def enter_username(self, user_name):
        self.driver.find_element_by_id(self.login_username_id).clear()
        self.driver.find_element_by_id(self.login_username_id).send_keys(user_name)

    def enter_password(self, pass_word):
        self.driver.find_element_by_id(self.login_password_id).clear()
        self.driver.find_element_by_id(self.login_password_id).send_keys(pass_word)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()



        