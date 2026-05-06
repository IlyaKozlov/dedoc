import unittest

from selenium.webdriver.chrome.webdriver import WebDriver

from ui_tests.pages.main_page import MainPage


class UiTests(unittest.TestCase):
    def setUp(self) -> None:
        """
        Function that runs before tests
        """
        super().setUp()
        self.driver = WebDriver()
        self.driver.get("http://localhost:1231")
        self.main_tab = self.driver.current_window_handle
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        super().tearDown()
        self.driver.quit()
