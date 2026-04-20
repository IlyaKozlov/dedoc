import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class TestUIClicker(unittest.TestCase):

    def setUp(self) -> None:
        """
        Function that runs before tests
        """
        super().setUp()
        self.driver = WebDriver()
        self.driver.get("http://localhost:1231")


    def test_document_type(self):
        div_xpath = '/html/body/form/div[1]/details/summary'
        self._click_element(div_xpath)
        xpath = '/html/body/form/div[1]/details/p[1]/label/select'
        self._click_element(xpath)
        xpath = '/html/body/form/div[1]/details/p[4]/label/select'
        self._click_element(xpath)
        xpath = '/html/body/form/div[1]/details/p[5]/label/select'
        self._click_element(xpath)
        self._click_element(div_xpath)

    def _click_element(self, xpath: str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

