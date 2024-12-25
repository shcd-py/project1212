from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTest:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup(self):
        self.driver = webdriver.Edge(self.driver_path)
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def login(self, url, username, password):
        try:
            self.setup()
            self.driver.get(url)
            time.sleep(2)
            self.driver.find_element(By.ID, "userName").send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.ID, "login").click()
            time.sleep(2)
            print("Login test completed.")
        finally:
            self.teardown()
