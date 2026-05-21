import unittest
from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver

from ui_tests.pages.main_page import MainPage
from ui_tests.pages.return_format import ReturnFormat


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

    def _upload_file(self,format:ReturnFormat):
        self.main_page.chose_return_format(format)
        file = Path(__file__).parent / ".." / "data" / "txt" / "example.txt"
        file = file.resolve()
        assert file.is_file()
        self.main_page.upload_file(file)