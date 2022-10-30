import json
import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.translate_page import TranslatePage
from utils.browser import Browser

LOGGER = logging.getLogger(__name__)


class TestTranslation:
    def read_data(self):
        """
        Opens up the translation.json file in the data directory
        Sets up to be used as values in the tests
        """
        with open('./data/translation.json') as file:
            self.data = json.load(file)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = Browser("Chrome", False).driver
        self.read_data()
        try:
            """
            Before All
            Selects source language from the drop-down menu on the left
            Selects translation language from the drop-down menu on the right
            Enters the initial text in the input field on the left
            """
            self.translation_page = TranslatePage(self.driver)
            self.translation_page.select_source_language_from_dropdown(self.data[0]['source_language'])
            self.translation_page.select_translation_language_from_dropdown(self.data[0]['translation_language'])
            self.translation_page.input_initial_text(self.data[0]['initial_text'])
            time.sleep(.5)

            # Run actual test
            yield
        finally:
            self.driver.quit()

    def test_valid_translation_from_source_to_target_language(self):
        """
        Verifies that the translation value is valid compared to the initial value
        """
        LOGGER.info(f'Translation Value - {self.translation_page.get_translation_value()}')
        LOGGER.info(f'Initial Value - {self.translation_page.get_initial_text_value()}')
        assert self.translation_page.get_translation_value() == self.data[0]['expected_result']

    def test_swap_language_feature(self):
        """
        Clicks the swap languages button
        Verifies the result of the translation language value and source language value
        """
        self.translation_page.swap_languages()
        time.sleep(1)
        LOGGER.info(f'Translation Value - {self.translation_page.get_translation_value()}')
        LOGGER.info(f'Initial Value - {self.translation_page.get_initial_text_value()}')
        assert self.translation_page.get_translation_value() == self.data[0]['initial_text']
        assert self.translation_page.get_initial_text_value() == self.data[0]['expected_result']

    def test_screen_keyboard(self):
        """
        Clears the input field (source language)
        Enters "hi!" using the on-screen keyboard
        """
        self.translation_page.clear_input_field()
        self.translation_page.type_hi_using_screen_keyboard()
