import random
import time
from importlib.resources import path
from pathlib import Path

from ui_tests.pages.return_format import ReturnFormat
from ui_tests.ui_tests_abc import UiTests
from selenium.webdriver.common.by import By

random.seed(42)


class TestReturnFormats(UiTests):

    def test_return_formats(self):
        formats = [r for r in ReturnFormat]
        file = Path(__file__).parent / ".." / "data" / "txt" / "example.txt"
        file = file.resolve()
        assert file.is_file()

        random.shuffle(formats)
        for format in formats:
            self.main_page.chose_return_format(format)
            self.main_page.upload_file(file)
            self.driver.back()
