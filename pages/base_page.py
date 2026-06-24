from helpers.helper import HelperPage
from pages.date_page import date_time
class BasePage(HelperPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.current_date, self.tomorrow_date = date_time.dateTime()