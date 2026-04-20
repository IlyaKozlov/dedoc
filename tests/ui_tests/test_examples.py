import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json


class TestExamples(unittest.TestCase):

    def setUp(self) -> None:
        """
        Function that runs before tests
        """
        super().setUp()
        self.driver = WebDriver()
        self.driver.get("http://localhost:1231")
        self.main_tab = self.driver.current_window_handle

    def test_useful_link(self):
        xpath = '/html/body/ul/li[1]/a'
        element = self.driver.find_element(By.XPATH, xpath)
        tabs = self.driver.window_handles
        element.click()

        supported_formats_tab = self.wait_windows(10, tabs)
        self.driver.switch_to.window(supported_formats_tab)

        result_xpath = '/html/body/ol[1]/li[1]/a[2]'
        self.check_result(result_xpath, supported_formats_tab)
        pass

    def check_result(self, result_xpath, supported_formats_tab):
        result_element = self.driver.find_element(By.XPATH, result_xpath)
        tabs = self.driver.window_handles
        result_element.click()

        result_tab = self.wait_windows( 10, tabs)
        self.driver.switch_to.window(result_tab)

        js_xpath = '/html/body/pre'
        js_element = self.driver.find_element(By.XPATH, js_xpath)
        json.loads(js_element.text)
        self.driver.close()
        self.driver.switch_to.window(supported_formats_tab)

    def wait_windows(self, timeout: float, tabs: list[str]) -> str:
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > len(tabs))
        new_tabs = self.driver.window_handles
        new_tab = [tab for tab in new_tabs if tab not in tabs][0]
        return new_tab