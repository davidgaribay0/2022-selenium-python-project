import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TranslatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = 'https://translate.google.com/'
        self.go_to(self.url)
        self.source_language_dropdown_locator = '[aria-label="More source languages"]'
        self.target_language_dropdown_locator = '[aria-label="More target languages"]'
        self.source_languages_partial_locator = '//*[@data-language-code]//div[2][text()='
        self.source_languages_index = 0
        self.target_languages_index = 1
        self.initial_input_locator = '//textarea'
        self.swap_languages_locator = '//*[starts-with(@aria-label,"Swap languages")]'
        self.translation_value_locator = '//div/span[@lang]'
        self.screen_keyboard_locator = '//*[starts-with(@aria-label,"Show the Input")]//preceding::a[1]'

    def select_source_language_from_dropdown(self, language):
        self.click(self.source_language_dropdown_locator)
        time.sleep(1)
        self.driver.find_elements(By.XPATH, f'{self.source_languages_partial_locator}"{language}"]')[
            self.source_languages_index].click()

    def select_translation_language_from_dropdown(self, language):
        self.click(self.target_language_dropdown_locator)
        time.sleep(1)
        self.driver.find_elements(By.XPATH, f'{self.source_languages_partial_locator}"{language}"]')[
            self.target_languages_index].click()

    def input_initial_text(self, text):
        self.type_using_xpath(self.initial_input_locator, text)

    def get_initial_text_value(self):
        return self.get_value_of_text_area(self.initial_input_locator)

    def swap_languages(self):
        self.click_using_xpath(self.swap_languages_locator)
        time.sleep(4)

    def get_translation_value(self):
        return self.get_value(self.translation_value_locator)

    def clear_input_field(self):
        self.click('[aria-label="Clear source text"')

    def select_screen_keyboard(self):
        self.click_using_xpath(self.screen_keyboard_locator)

    def type_hi_using_screen_keyboard(self):
        self.click_text("h")
        self.click_text("i")
        self.click_text("!")