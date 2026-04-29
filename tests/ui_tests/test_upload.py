import unittest
from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.main_page import MainPage


class TestUpload(unittest.TestCase):

    def setUp(self) -> None:
        """
        Function that runs before tests
        """
        super().setUp()
        self.driver = WebDriver()
        self.driver.get("http://localhost:1231")
        self.main_page= MainPage(self.driver)

    def test_upload_file(self):
        path = Path(__file__).parent.parent / "data"/ "txt" / "example.txt"
        assert path.exists()
        self.main_page.choose_file(path)
        self.main_page.click_upload()
        pass
