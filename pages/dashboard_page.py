from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:


    PRODUCT_TITLE = (By.CLASS_NAME, "app_logo")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_dashboard_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.PRODUCT_TITLE))
            return True
        except:
            return False
        
    def product_count(self):
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)