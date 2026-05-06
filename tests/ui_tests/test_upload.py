from pathlib import Path

from ui_tests.ui_tests_abc import UiTests


class TestUpload(UiTests):

    def test_upload_file(self):
        path = Path(__file__).parent.parent / "data"/ "txt" / "example.txt"
        self.main_page.upload_file(path)

    def test_upload_wrong_file(self):
        path = Path(__file__).parent.parent / "data"/ "file.bin"
        self.main_page.upload_file(path)
        pass
