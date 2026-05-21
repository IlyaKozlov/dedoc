from selenium.webdriver.common.by import By

from ui_tests.pages.dociment_type import DocumentType
from ui_tests.pages.return_format import ReturnFormat
from ui_tests.ui_tests_abc import UiTests


class TestDocumentTypes(UiTests):
    def test_document_types(self):

        doc_types = [t for t in DocumentType]

        for doc_type in doc_types:
            self.main_page.chose_document_type(doc_type)
            self._upload_file(ReturnFormat.JSON)
            self.driver.back()