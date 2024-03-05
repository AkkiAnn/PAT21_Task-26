import pytest
from selenium import webdriver

driver = None
driver_path = (r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")
imdb_url = "https://www.imdb.com/search/name/"

@pytest.fixture(scope="class")
def chrome_driver(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(imdb_url)
    request.cls.driver = imdb_url

    yield driver
    # Teardown Chrome driver
    driver.quit()