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
        self.screen_keyboard_shift_key_locator = '[id="K16"]'
        self.clear_source_text_input_locator = '[aria-label="Clear source text"'

    def select_source_language_from_dropdown(self, language):
        """
        Opens up the dropdown menu on the left (source language) and selects the value of language
        :param language: the language that will be selected
        """
        self.click(self.source_language_dropdown_locator)
        self.load_and_click_at_index(self.source_languages_index,
                                     f'{self.source_languages_partial_locator}"{language}"]')

    def select_translation_language_from_dropdown(self, language):
        """
        # Opens up the dropdown menu on the right (translation language) and selects the value of language
        :param language: the language that will be selected
        """
        self.click(self.target_language_dropdown_locator)
        self.load_and_click_at_index(self.target_languages_index,
                                     f'{self.source_languages_partial_locator}"{language}"]')

    def input_initial_text(self, text):
        """
        Inputs the value of text into the input field on the left (source language)
        :param text: will be typed out into the input field
        """
        self.type_using_xpath(self.initial_input_locator, text)

    def get_initial_text_value(self):
        """
        Reads the value that is in the left input field (source language)
        :return: the initial text value
        """
        return self.get_value_of_text_area(self.initial_input_locator)

    def swap_languages(self):
        """
        Clicks on the swap language button
        """
        self.click_using_xpath(self.swap_languages_locator)

    def get_translation_value(self):
        """
        Reads the value that is in the right input field (translation language)
        :return: translation value
        """
        return self.get_value(self.translation_value_locator)

    def clear_input_field(self):
        """
        Clears the left input field (source language)
        """
        self.click(self.clear_source_text_input_locator)

    def type_hi_using_screen_keyboard(self):
        """
        Opens up the on-screen keyboard and enters "hi!"
        """
        self.click_using_xpath(self.screen_keyboard_locator)
        self.click_text("h")
        self.click_text("i")
        self.click(self.screen_keyboard_shift_key_locator)
        self.click_text("!")
