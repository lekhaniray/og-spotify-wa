from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import unittest
import datetime
from pages.account_page_spotify import AccountPage
from pages.login_spotify import LoginPage
from pages.homePage_spotify import HomePage
from pages.search_page import searchPage

path = "/home/lekhaniray/Downloads/chromedriver_linux64/chromedriver"
base_url = "https://open.spotify.com/"


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        action = ActionChains(self.driver)
        print("-------------------------------------------------------------")
        print("Test Environment created")
        print("Run started at:" + str(datetime.datetime.now()))


    def test_loginSpotify(self):

        driver = self.driver

        self.driver.get(base_url)
        self.assertIn("Spotify", driver.title)
        print(self.driver.title)

        home_page = HomePage(driver)
        home_page.click_homepage_login()

        login = LoginPage(driver)
        login.enter_username("lekhaniray@yahoo.com")
        login.enter_password("r@nd0m12345")
        login.click_login()

        account_page_actions = AccountPage(driver)
        account_page_actions.remove_cookie_policy()
        account_page_actions.musicPlayer_play()
        sleep(10)
        account_page_actions.musicPlayer_next()
        sleep(10)
        account_page_actions.musicPlayer_previous()
        sleep(10)
        account_page_actions.musicPlayer_enableShuffle()
        account_page_actions.musicPlayer_enableRepeat()
        account_page_actions.search_function()
        

        search_page = searchPage(driver)
        search_page.search_song("Taylor Swift")
        sleep(10)



    def tearDown(self):
        if(self.driver != None):
            print("-------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output= '/home/lekhaniray/spotify-wa-project/TestResults'))