from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.page_abc import Page


class MainPage(Page):

    def choose_file(self, path: Path):
        xpath = '/html/body/form/div[5]/div[1]/input'
        upload_element = self._driver.find_element(By.XPATH, xpath)
        upload_element.send_keys(
            str(path)
        )

    def click_upload(self):
        xpath = '/html/body/form/div[5]/div[2]/input'
        element = self._driver.find_element(By.XPATH, xpath)
        element.click()

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