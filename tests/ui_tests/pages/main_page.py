from pathlib import Path

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


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
