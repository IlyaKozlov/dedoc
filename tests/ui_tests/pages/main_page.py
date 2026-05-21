from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.dociment_type import DocumentType
from ui_tests.pages.page_abc import Page
from ui_tests.pages.return_format import ReturnFormat


class MainPage(Page):
    _form_xpath = '/html/body/form/div[1]/details/p[5]/label/select'

    def choose_file(self, path: Path):
        xpath = '/html/body/form/div[5]/div[1]/input'
        upload_element = self._driver.find_element(By.XPATH, xpath)
        upload_element.send_keys(
            str(path)
        )

    def wait_result(self):
        url = 'http://localhost:1231/upload'
        WebDriverWait(self._driver, 3).until(lambda d: self._driver.current_url == url)

    def click_upload(self):
        xpath = '/html/body/form/div[5]/div[2]/input'
        element = self._driver.find_element(By.XPATH, xpath)
        element.click()
        self.wait_result()

    def click_useful_link(self) -> str:
        xpath = '/html/body/ul/li[1]/a'
        element = self._driver.find_element(By.XPATH, xpath)
        tabs = self._driver.window_handles
        element.click()

        supported_formats_tab = self.wait_windows(10, tabs)
        self._driver.switch_to.window(supported_formats_tab)
        return supported_formats_tab


    def upload_file(self, path: Path):
        assert path.is_file()
        self.choose_file(path)
        self.click_upload()

    def chose_return_format(self, format: ReturnFormat):
        self._check_displayed()
        format_dropdown = self._driver.find_element(By.XPATH, self._form_xpath)
        format_dropdown.click()

        chose_xpath = f'/html/body/form/div[1]/details/p[5]/label/select/option[{format.value}]'
        element = self._driver.find_element(By.XPATH, chose_xpath)
        element.click()

    def _check_displayed(self):
        format_dropdown = self._driver.find_element(By.XPATH, self._form_xpath)
        if not format_dropdown.is_displayed():
            open_xpath = '/html/body/form/div[1]/details/summary'
            element = self._driver.find_element(By.XPATH, open_xpath)
            element.click()

    def chose_document_type(self, doc_type: DocumentType):
        self._check_displayed()
        doc_xpath = '/html/body/form/div[1]/details/p[1]/label/select'
        doc_type_dropdown = self._driver.find_element(By.XPATH, doc_xpath)
        doc_type_dropdown.click()
        doc_type_xpath = f'/html/body/form/div[1]/details/p[1]/label/select/option[{doc_type.value}]'
        doc_type_element = self._driver.find_element(By.XPATH, doc_type_xpath)
        doc_type_element.click()