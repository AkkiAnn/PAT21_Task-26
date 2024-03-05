from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.configuration import CommonPage as CP




class Imdb_Page(CP):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

    # Entering the data_name
    def name_data(self, enter_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.NAME_DD))(self.CP.click())
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.name_value()))(self.CP.send_key(enter_name))

    # Entering the data_birth_date (mm/dd/yyyy).
    def birth_date_data(self, from_date, to_date):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BIRTHDATE_DD))(self.CP.click())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birthdate1_value()))(self.CP.send_key(from_date))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.birthdate2_value()))(self.CP.send_key(to_date))

    # Entering the data_birthday(mm/dd).
    def birthday_data(self, birth_date):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BIRTHDATE_DD))(self.CP.click())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.bd_value()))(self.CP.send_key(birth_date))

    # Select data_award
    def awards_data(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.AWARDS_RECOGNITION_DD))(self.CP.click())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.award_rec_value()))(self.CP.click())

    # Page topic data(eg:Biography)
    def page_topic_data(self,enter_bio):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PAGE_TOPIC_DD))(self.CP.click())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.page_topic__value()))(self.CP.send_key(enter_bio))


    # Select gender (M/F/O)
    def gender_id(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.GENDER_IDENTITY_DD))(self.CP.click())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.gender_identity_value()))(self.CP.click())

    # Credits
    def credits(self,movie_name):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CREDITS_DD))(self.CP.click())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.credits_value()))(self.CP.send_key(movie_name))

    # Adult data_name
    def adult_name(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADULT_NAME_DD))(self.CP.click())
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.adult_name_value()))(self.CP.click())

    # Final operation of see_result button
    def search(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_BUTTON))(self.CP.click())

    # Page_scroll_down where we want to need.
    def scroll_down(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)))