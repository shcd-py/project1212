from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class ButtonTest:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        self.driver = webdriver.Edge(self.driver_path)
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def test_buttons(self, url):
        try:
            self.setup()
            self.driver.get(url)
            time.sleep(2)
            action = ActionChains(self.driver)

            # Double click
            double_click_btn = self.driver.find_element(By.ID, "doubleClickBtn")
            action.double_click(double_click_btn).perform()
            print("Double click performed.")

            # Right click
            right_click_btn = self.driver.find_element(By.ID, "rightClickBtn")
            action.context_click(right_click_btn).perform()
            print("Right click performed.")

            # Single click
            single_click_btn = self.driver.find_element(By.XPATH, "//button[text()='Click Me']")
            single_click_btn.click()
            print("Single click performed.")
        finally:
            self.teardown()
