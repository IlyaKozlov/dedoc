import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import json

from ui_tests.pages.main_page import MainPage


class TestExamples(unittest.TestCase):

    def setUp(self) -> None:
        """
        Function that runs before tests
        """
        super().setUp()
        self.driver = WebDriver()
        self.driver.get("http://localhost:1231")
        self.main_tab = self.driver.current_window_handle
        self.main_page = MainPage(self.driver)

    def test_result_link(self):
        supported_formats_tab = self.main_page.click_useful_link()
        result_link_elements = self.driver.find_elements(By.LINK_TEXT, 'result')
        for link in result_link_elements:
            self.check_result(link,supported_formats_tab)

    def test_result_html_link(self):
        supported_formats_tab = self.main_page.click_useful_link()
        result_link_element = self.driver.find_elements(By.LINK_TEXT, 'result in html')
        for link in result_link_element:
            self.check_result_html(link, supported_formats_tab)


    def check_result(self, element: WebElement, supported_formats_tab: str):
        self.click_on_link(element)
        js_xpath = '/html/body/pre'
        js_element = self.driver.find_element(By.XPATH, js_xpath)
        json.loads(js_element.text)

        self.close_tab(supported_formats_tab)

    def check_result_html(self, element: WebElement, supported_formats_tab: str):
        self.click_on_link(element)
        html_xpath = '/html/body/p[1]/sub'
        html_element = self.driver.find_element(By.XPATH, html_xpath)
        self.assertEqual(html_element.text, 'id = 0 ; type = root')

        self.close_tab(supported_formats_tab)


    def click_on_link(self, element: WebElement):
        tabs = self.driver.window_handles
        element.click()

        result_tab = self.main_page.wait_windows(10, tabs)
        self.driver.switch_to.window(result_tab)

    def close_tab(self,supported_formats_tab:str):
        self.driver.close()
        self.driver.switch_to.window(supported_formats_tab)


    def tearDown(self):
        super().tearDown()
        self.driver.quit()

