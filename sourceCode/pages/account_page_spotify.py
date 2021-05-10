from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
class AccountPage():


    def __init__(self, driver):
        self.driver = driver
        self.policy_close_button_xpath = "//*[@id='onetrust-close-btn-container']/button"
        self.music_play_button_xpath = "//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]"
        self.music_next_button_xpath = "//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[4]"
        self.music_previous_button_xpath = "//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[2]"
        self.music_shuffle_button_xpath = "//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[1]"
        self.music_repeat_button_xpath = "//*[@id='main']/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[5]"
        self.music_search_xpath = "//*[@id='main']/div/div[2]/nav/div[1]/div[2]/div/div[1]/button"


    def remove_cookie_policy(self):
        #Wait for the cookie message
        close_icon = WebDriverWait(self.driver, 5, 0.25).until(EC.visibility_of_element_located([By.XPATH, self.policy_close_button_xpath]))
        close_icon.click()
        #Wait for the cookie message to disappear
        WebDriverWait(self.driver, 5, 0.25).until(EC.visibility_of_element_located([By.XPATH, self.policy_close_button_xpath]))
        link = self.driver.find_element_by_xpath(self.policy_close_button_xpath)
        link.click()

    def musicPlayer_play(self):
        self.driver.find_element_by_xpath(self.music_play_button_xpath).click()
        

    def musicPlayer_next(self):
        self.driver.find_element_by_xpath(self.music_next_button_xpath).click()
        
    
    def musicPlayer_previous(self):
        self.driver.find_element_by_xpath(self.music_previous_button_xpath).click()

    def musicPlayer_enableShuffle(self):
        self.driver.find_element_by_xpath(self.music_shuffle_button_xpath).click()


    def musicPlayer_enableRepeat(self):
        self.driver.find_element_by_xpath(self.music_repeat_button_xpath).click()

    def search_function(self):
        self.driver.find_element_by_xpath(self.music_search_xpath).click()


                

        
   

    
   