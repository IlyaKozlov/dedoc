import random
import time
from importlib.resources import path
from pathlib import Path
import json

from api.schema import ParsedDocument
from ui_tests.pages.json_page import JsonPage
from ui_tests.pages.return_format import ReturnFormat
from ui_tests.ui_tests_abc import UiTests
from selenium.webdriver.common.by import By

random.seed(42)


class TestReturnFormats(UiTests):

    def test_return_formats(self):
        formats = [r for r in ReturnFormat]

        random.shuffle(formats)
        for format in formats:
            self._upload_file(format)
            self.driver.back()

    def test_return_json_format(self):

        for format in [ReturnFormat.JSON, ReturnFormat.PRETTY_JSON]:
            self._upload_file(format)

            json_page = JsonPage(self.driver)
            result = json.loads(json_page.get_json())
            ParsedDocument.model_validate(result)
            self.driver.back()

    def _upload_file(self,format:ReturnFormat):
        self.main_page.chose_return_format(format)
        file = Path(__file__).parent / ".." / "data" / "txt" / "example.txt"
        file = file.resolve()
        assert file.is_file()
        self.main_page.upload_file(file)