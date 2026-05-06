from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

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

    def wait_windows(self, timeout: float, tabs: list[str]) -> str:
        WebDriverWait(self._driver, timeout).until(lambda d: len(d.window_handles) > len(tabs))
        new_tabs = self._driver.window_handles
        new_tab = [tab for tab in new_tabs if tab not in tabs][0]
        return new_tab
