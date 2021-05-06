from selenium import webdriver
from time import sleep
import unittest
import datetime

path = "/home/lekhaniray/Downloads/chromedriver_linux64/chromedriver"

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        print("-------------------------------------------------------------")
        print("Test Environment created")
        print("Run started at:" + str(datetime.datetime.now()))

    def test_navigateSpotify(self):

        self.driver.get("https://www.spotify.com/us/")
        print(self.driver.title)
        self.driver.maximize_window()
        self.driver.find_element_by_link_text("Log in").click()
        sleep(2)
        username = self.driver.find_element_by_id("login-username")
        username.clear()
        username.send_keys("lekhaniray@yahoo.com")

        password = self.driver.find_element_by_id("login-password")
        password.clear()
        password.send_keys("r@nd0m12345")
        self.driver.find_element_by_id("login-button").click()

        sleep(4)






    def tearDown(self):
        if(self.driver!= None):
            print("-------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()