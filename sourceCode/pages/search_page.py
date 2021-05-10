class searchPage():
    def __init__(self, driver):
        self.driver = driver
        self.search_field_xpath = "//*[@id='main']/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[3]/section/div/div/input"

    def search_song(self, artist_name):
        self.driver.find_element_by_xpath(self.search_field_xpath).send_keys(artist_name)



