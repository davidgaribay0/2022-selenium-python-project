import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.translate_page import TranslatePage
import logging
import time

LOGGER = logging.getLogger(__name__)


def test_translation():
    with open('./data/translation.json') as fixture:
        data = json.load(fixture)
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_size(1920, 1080)
    try:
        translation_page = TranslatePage(driver)
        translation_page.select_source_language_from_dropdown(data[0]['sourceLanguage'])
        time.sleep(1)
        translation_page.select_translation_language_from_dropdown(data[0]['translationLanguage'])
        translation_page.input_initial_text(data[0]['initialText'])
        time.sleep(10)
        assert translation_page.get_translation_value() == data[0]['expectedResult']
        LOGGER.info(f'Translation Value - {translation_page.get_translation_value()}')
        LOGGER.info(f'Initial Value - {translation_page.get_initial_text_value()}')

    finally:
        driver.quit()
    #
    # time.sleep(1)
    # translation_page.swap_languages()
    # time.sleep(5)
