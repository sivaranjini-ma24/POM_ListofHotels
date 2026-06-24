import pytest
from config import Config
from pages.home_page import HomePage

def test_get_mumbai_hotels(driver):
    home_page = HomePage(driver)
    home_page.URL(Config.BASE_URL)
    
    home_page.close_initial_popups()
    home_page.navigate_to_hotels()
    home_page.search_hotels_for_mumbai()
    home_page.select_travel_dates()
    
    hotel_list = home_page.get_hotel_names()
    assert len(hotel_list) > 0, "No hotels were found in the search results!"
