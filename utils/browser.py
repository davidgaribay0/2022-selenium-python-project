from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, name, is_headless):
        self.name = name
        self.is_headless = is_headless
        if name == "Chrome":
            options = Options()
            if is_headless:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            self.driver.set_window_size(1920, 1080)
