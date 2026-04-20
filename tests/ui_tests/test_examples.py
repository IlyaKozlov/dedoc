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
        element.click()

        self.wait_windows(self.driver, 10, 1)
        new_tab = self.wait_windows(self.driver, self.main_tab)
        self.driver.switch_to.window(new_tab)

        result_xpath = '/html/body/ol[1]/li[1]/a[2]'
        result_element = self.driver.find_element(By.XPATH, result_xpath)
        result_element.click()

        self.wait_windows(self.driver, 10,2)
        new_tab = self.wait_windows(self.driver, self.main_tab)
        self.driver.switch_to.window(new_tab)

        js_xpath = '/html/body/pre'
        js_element = self.driver.find_element(By.XPATH, js_xpath)
        json.loads(js_element.text)
        pass


    def wait_windows(self, driver, timeout, min_window):
        WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) > min_window)
        tabs = self.driver.window_handles
        new_tab = [tab for tab in tabs if tab != self.main_tab][0]
        return new_tab