from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date, timedelta
from datetime import datetime, timedelta

class date_time:
        @staticmethod
        def dateTime():
                current_date_str = datetime.now().strftime("%a %b %d %Y") # Example: 'Mon Jun 22 2026'
                print(f"Dynamically selecting today's date: {current_date_str}")
                today = datetime.now()
                # Add 1 day to get tomorrow
                tomorrow = today + timedelta(days=1)
                # Format the date (Thu Jun 25 2026  website's format)
                tomorrow_formatted = tomorrow.strftime("%a %b %d %Y") 
                print(f"Tomorrow's date is: {tomorrow_formatted}")
                return current_date_str,tomorrow_formatted