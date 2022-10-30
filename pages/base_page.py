import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def go_to(self, url):
        """
        Navigates to directly to the url specified
        :param url: valid full url of webpage
        """
        self.driver.get(url)

    def type(self, element, text):
        """
        Types characters into a given element (located using css selector)
        :param element: CSS selector locator
        :param text: value that will be typed into element
        """
        element = self.driver.find_element(By.CSS_SELECTOR, element)
        element.click()
        element.send_keys(text)

    def type_using_xpath(self, element, text):
        """
        Types characters into a given element (located using XPath)
        :param element: XPath locator
        :param text: value that will be typed into element
        """
        element = self.driver.find_element(By.XPATH, element)
        element.click()
        element.send_keys(text)

    def click(self, element):
        """
        Clicks on element that is located using css selector
        :param element: css selector locator
        """
        time.sleep(.5)
        element = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, element))
        )
        element.click()
        time.sleep(.5)

    def click_using_xpath(self, element):
        """
        Clicks on element that is located using XPath selector
        :param element: XPath locator
        """
        self.wait_until_xpath_located(element).click()

    def get_value(self, element):
        """
        Returns the value (text) of an element that is located using XPath
        :param element: XPath locator
        :return: text of element
        """
        return self.wait_until_xpath_located(element).text

    def get_value_of_text_area(self, element):
        """
        Returns the value of a given textarea
        :param element: XPath locator
        :return: value of textarea
        """
        return self.wait_until_xpath_located(element).get_attribute("value")

    def click_text(self, text):
        """
        Clicks an element that is located by using it text value
        :param text: display text of element
        """
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="{text}"]')))
        element.click()

    def wait_until_xpath_located(self, locator):
        """
        Waits until the presence of an element is detected
        :param locator: XPath locator
        :return: web element
        """
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
