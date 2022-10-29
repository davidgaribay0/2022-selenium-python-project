from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def go_to(self, url):
        self.driver.get(url)

    def type(self, element, text):
        element = self.driver.find_element(By.CSS_SELECTOR, element)
        element.click()
        element.send_keys(text)

    def type_using_xpath(self, element, text):
        element = self.driver.find_element(By.XPATH, element)
        element.click()
        element.send_keys(text)

    def click(self, element):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element))
        )
        element.click()

    def click_using_xpath(self, element):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, element))
        )
        element.click()

    def get_value(self, element):
        element = self.driver.find_element(By.XPATH, element)
        return element.text

    def get_value_of_text_area(self, element):
        element = self.driver.find_element(By.XPATH, element)
        return element.get_attribute("value")

    def click_text(self, text):
        element = self.driver.find_element(By.XPATH, f'//*[text()="{text}"]')
        element.click()

    def find_all_by_attribute_name(self, attribute_name):
        return self.driver.find_elements(By.XPATH, attribute_name)
