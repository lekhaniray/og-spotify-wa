from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
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
        action = ActionChains(self.driver)
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

        try:
            WebDriverWait(driver, 40).until(EC.alert_is_present(),
            'Timed out waiting for PA creation ' +
            'confirmation popup to appear.')
            alert = self.driver.switch_to.alert()
            alert.accept()

        except:
            print("Did not work")

        sleep(3)


    def test_navigateSpotify(self):

        self.driver.get("https://open.spotify.com/")
        print(self.driver.title)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/header/div[5]/button[2]").click()
        sleep(2)
        username = self.driver.find_element_by_id("login-username")
        username.clear()
        username.send_keys("lekhaniray@yahoo.com")

        password = self.driver.find_element_by_id("login-password")
        password.clear()
        password.send_keys("r@nd0m12345")
        self.driver.find_element_by_id("login-button").click()
        sleep(5)

        sleep(5)


        #Wait for the cookie message
        close_icon = WebDriverWait(self.driver, 5, 0.25).until(EC.visibility_of_element_located([By.XPATH, "//*[@id='onetrust-close-btn-container']/button"]))
        close_icon.click()
        #Wait for the cookie message to disappear
        WebDriverWait(self.driver, 5, 0.25).until(EC.visibility_of_element_located([By.XPATH, "//*[@id='onetrust-close-btn-container']/button"]))
        link = self.driver.find_element_by_xpath("//*[@id='onetrust-close-btn-container']/button")
        link.click()
       

        
    #    play_button = self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]")
    #    self.driver.execute_script("arguments[0].click();", play_button)
        self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]").click()
        sleep(10)
        self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[4]").click()
        sleep(10)


#        forward_button = self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[4]/svg")
#        self.driver.execute_script("arguments[0].click();", forward_button)
        

      
 #       self.clearPopUps()

#        action = webdriver.common.action_chains.ActionChains(driver)
#        action.move_to_element_with_offset(el, 0, 0)
#        action.click()
#        action.perform()
        


    def tearDown(self):
        if(self.driver!= None):
            print("-------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()