import json

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from ui_tests.pages.supported_formats_page import SupportedFormatsPage
from ui_tests.ui_tests_abc import UiTests


class TestExamples(UiTests):

    def setUp(self) -> None:
        super().setUp()
        self.supported_formats_tab = self.main_page.click_useful_link()
        self.sf_page = SupportedFormatsPage(self.driver)

    def test_result_link(self):
        result_link_elements = self.driver.find_elements(By.LINK_TEXT, 'result')
        for link in result_link_elements:
            self.check_result(link,self.supported_formats_tab)

    def test_result_html_link(self):
        result_link_element = self.driver.find_elements(By.LINK_TEXT, 'result in html')
        for link in result_link_element:
            self.check_result_html(link, self.supported_formats_tab)


    def check_result(self, element: WebElement, supported_formats_tab: str):
        self.sf_page.click_on_link(element)
        js_xpath = '/html/body/pre'
        js_element = self.driver.find_element(By.XPATH, js_xpath)
        json.loads(js_element.text)

        self.sf_page.close_tab(supported_formats_tab)

    def check_result_html(self, element: WebElement, supported_formats_tab: str):
        self.sf_page.click_on_link(element)
        html_xpath = '/html/body/p[1]/sub'
        html_element = self.driver.find_element(By.XPATH, html_xpath)
        self.assertEqual(html_element.text, 'id = 0 ; type = root')

        self.sf_page.close_tab(supported_formats_tab)





