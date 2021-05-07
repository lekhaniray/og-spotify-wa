from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
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

    def clearPopUps(self):
        try:
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[12]/div/div/div/div[2]/button[2]").click()
        except:
            print("No button")
            pass 
        
        try:
            alert = self.driver.switch_to.alert()
            alert.dismiss()
        except:
            print("pass")
            pass

        sleep(3)


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
       


 #       self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]").click()
        

      
        self.clearPopUps()

        sleep(4)

        button = self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]")
        self.driver.execute_script("arguments[0].click();", button)


    def tearDown(self):
        if(self.driver!= None):
            print("-------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()