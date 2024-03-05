import pytest
from config.configuration import CommonPage
from pages.imdb import Imdb_Page
from test_cases.conftest import chrome_driver

@pytest.mark.usefixtures('chrome_driver')
class Test_Imdb(CP):
    def test_see_results(self):

        self.imdb = Imdb_Page(self.driver)

        # Enter the name in name field
        self.imdb.name_data('Tom Cruise')


        # Enter the brith_date in brith_date field
        self.imdb.birth_date_data('03/07/1962', '03/07/2024')

        self.imdb.scroll_down()

        # Enter the birth_day_date in brith_day_date field
        self.imdb.birthday_data('07-03')


        # Select options as per our need in Awards & recognition field
        self.imdb.awards_data()

        self.imdb.scroll_down()

        # Enter the page_topic in the page_topic field
        self.imdb.page_topic_data("Movies")


        self.imdb.scroll_down()

        # Select the Gender in the Gender field
        self.imdb.gender_id()


        # Enter the Credits in the Credits Field
        self.imdb.credits('The Mummy')

        self.imdb.scroll_down()

        # Select the Adult_Name as per need or not in adult_name field
        self.imdb.adult_name()

        # Hit the see result button
        self.imdb.search()

        expected_url = ('https://www.imdb.com/search/name/?name=Tom%20Cruise&birth_date=1962-07-03,1962-07-03&birth_monthday=07-03&groups=oscar_best_actor_nominees&has=bio&gender=male&roles=tt2345759&adult=include')


        assert self.driver.current_url == expected_url, "Somthing Went Wrong"