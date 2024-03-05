from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CommonPage:

    def __init__(self, driver):
        self.driver = driver

    NAME_DD = (By.XPATH, '//*[@id="nameTextAccordion"]/div[1]/label/span[1]/div')
    name_value = (By.NAME, 'name-text-input')
    BIRTHDATE_DD = (By.XPATH, '//*[@id="birthDateAccordion"]/div[1]/label')
    birthdate1_value = (By.NAME, 'birth-date-start-input')
    birthdate2_value = (By.NAME, 'birth-date-end-input')
    BIRTHDAY_DD = (By.XPATH, '//*[@id="birthdayAccordion"]/div[1]/label')
    bd_value = (By.NAME, 'birthday-input')
    AWARDS_RECOGNITION_DD = (By.XPATH, '//*[@id="awardsAccordion"]/div[1]/label')
    award_rec_value = (By.XPATH, '//*[@id="accordion-item-awardsAccordion"]/div/section/button[2]')
    PAGE_TOPIC_DD = (By.XPATH, '//*[@id="pageTopicsAccordion"]/div[1]/label')
    page_topic_value1 = (By.XPATH, '// *[ @ id = "accordion-item-pageTopicsAccordion"] / div / div / section / button[2]')
    page_topic_value2 = (By.XPATH, '//*[@id="accordion-item-pageTopicsAccordion"]/div/div/section/button[1]')
    DROP_DOWN_DD = (By.XPATH, '//*[@id="within-topic-dropdown-id"]')
    dd_value = (By.NAME, 'within-topic-input')
    GENDER_IDENTITY_DD = (By.XPATH, '//*[@id="genderIdentityAccordion"]/div[1]/label')
    gender_identity_value = (By.XPATH, '//*[@id="accordion-item-genderIdentityAccordion"]/div/section/button[1]')
    CREDITS_DD = (By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label')
    credits_value = (By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')
    ADULT_NAME_DD = (By.XPATH, '//*[@id="adultNamesAccordion"]/div[1]/label')
    adult_name_value = (By.ID, 'include-adult-names')
    SEARCH_BUTTON = (By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button[2]')

    # Send_keys Block
    def send_key(self,by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Click Block
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()


