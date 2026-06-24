from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pages.base_page import BasePage
from pages.date_page import date_time

class HomePage(BasePage,date_time):
    # Locators
    MODAL_CLOSE_BTN = (By.XPATH, "//*[@data-cy='closeModal']")
    HOTELS_MENU_TAB = (By.XPATH, "//li[@class='menu_Hotels']")
    CITY_SEARCH_TRIGGER = (By.ID, "city")
    CITY_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Where do you want to stay?']")
    FIRST_CITY_SUGGESTION = (By.XPATH, "//ul[@role='listbox']/li[1] | //p[contains(text(),'Mumbai')]")
    # Today_date=(By.XPATH, f"//div[@aria-label={date_time.dateTime.current_date}]")
    # Tommorrow_date=(By.XPATH, "//div[@aria-label='self.tomorrow_date']")
    Apply=(By.XPATH,"//*[@data-cy='RoomsGuestsNew_327']")
    SEARCH_BUTTON = (By.ID, "hsw_search_button")
    HOTEL_NAMES_LIST = (By.XPATH, "//span[@id='det_heading_hotelName']")

    def close_initial_popups(self):
        # Closes any initial login popups if they appear
        try:
            self.click(self.MODAL_CLOSE_BTN)
        except Exception:
            pass # Skip if popup doesn't show up

    def navigate_to_hotels(self):
        self.click(self.HOTELS_MENU_TAB)

    def search_hotels_for_mumbai(self):
        self.click(self.CITY_SEARCH_TRIGGER)
        self.sendKeys(self.CITY_INPUT_FIELD, "Mumbai")
        # time.sleep(2) # Brief pause for search dropdown to populate
        self.findElement(self.FIRST_CITY_SUGGESTION)
        self.click(self.FIRST_CITY_SUGGESTION)

        # time.sleep(5) # Wait for page load and listings to populate
    def get_today_date_locator(self):
        """Generates the locator dynamically using the current date string from BasePage."""
        return (By.XPATH, f"//div[@aria-label='{self.current_date}']")

    def get_tomorrow_date_locator(self):
        """Generates the locator dynamically using the tomorrow date string from BasePage."""
        return (By.XPATH, f"//div[@aria-label='{self.tomorrow_date}']")

    # --- Page Actions ---
    def select_travel_dates(self):
        """Action method to handle the date selection flow."""
        # 1. Click today's date
        today_locator = self.get_today_date_locator()
        self.findElement(today_locator)
        self.click(today_locator)
        # 2. Click tomorrow's date
        tomorrow_locator = self.get_tomorrow_date_locator()
        self.findElement(tomorrow_locator)
        self.click(tomorrow_locator)
        self.actionChains(self.Apply)
        self.findElement(self.Apply)
        self.click(self.Apply)
        self.click(self.SEARCH_BUTTON)
    def get_hotel_names(self):
        elements = self.findElements(self.HOTEL_NAMES_LIST)
        return [element.text for element in elements if element.text]
