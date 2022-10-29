import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.translate_page import TranslatePage
import logging
import time

LOGGER = logging.getLogger(__name__)


class TestTranslation:
    def read_data(self):
        with open('./data/translation.json') as file:
            self.data = json.load(file)

    @pytest.fixture(autouse=True)
    def setup(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.set_window_size(1920, 1080)
        self.read_data()
        try:
            # Before All
            self.translation_page = TranslatePage(self.driver)
            self.translation_page.select_source_language_from_dropdown(self.data[0]['sourceLanguage'])
            time.sleep(1)
            self.translation_page.select_translation_language_from_dropdown(self.data[0]['translationLanguage'])
            self.translation_page.input_initial_text(self.data[0]['initialText'])
            time.sleep(10)

            # Run actual test
            yield
        finally:
            self.driver.quit()

    def test_valid_translation_from_source_to_target_language(self):
        LOGGER.info(f'Translation Value - {self.translation_page.get_translation_value()}')
        LOGGER.info(f'Initial Value - {self.translation_page.get_initial_text_value()}')
        assert self.translation_page.get_translation_value() == self.data[0]['expectedResult']

    def test_swap_language_feature(self):
        self.translation_page.swap_languages()
        time.sleep(2)
        LOGGER.info(f'Translation Value - {self.translation_page.get_translation_value()}')
        LOGGER.info(f'Initial Value - {self.translation_page.get_initial_text_value()}')
        assert self.translation_page.get_translation_value() == self.data[0]['initialText']
        assert self.translation_page.get_initial_text_value() == self.data[0]['expectedResult']

    def test_screen_keyboard(self):
        self.translation_page.clear_input_field()
        time.sleep(1)
        self.translation_page.select_screen_keyboard()
        time.sleep(1)
        self.translation_page.type_hi_using_screen_keyboard()
        time.sleep(100)
