from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date, timedelta
from datetime import datetime, timedelta
import time

class HelperPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,30)
    def URL(self,url):
        self.driver.get(url)
    def findElement(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    def findElements(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    def click(self,locator):
        element= self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    def sendKeys(self,locator,text):
        element=self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)
    def actionChains(self,locator):
        # self.wait.until(EC.visibility_of_element_located(locator))
        time.sleep(5)
        actions=ActionChains(self.driver)
        actions.scroll_to_element(self.driver.find_element(*locator)).perform()
    def dateTime(self):
        current_date_str = datetime.now().strftime("%a %b %d %Y") # Example: 'Mon Jun 22 2026'
        print(f"Dynamically selecting today's date: {current_date_str}")
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime("%a %b %d %Y") 
        print(f"Tomorrow's date is: {tomorrow_formatted}")
        return current_date_str,tomorrow_formatted   
        print("Time")
    

