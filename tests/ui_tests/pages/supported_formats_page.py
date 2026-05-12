from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from ui_tests.pages.page_abc import Page


class SupportedFormatsPage(Page):

    def click_on_link(self, element: WebElement):
        tabs = self._driver.window_handles
        element.click()

        result_tab = self.wait_windows(10, tabs)
        self._driver.switch_to.window(result_tab)

    def close_tab(self,supported_formats_tab:str):
        self._driver.close()
        self._driver.switch_to.window(supported_formats_tab)

    def get_result_elements(self) -> list[WebElement]:
        result_link_elements = self._driver.find_elements(By.LINK_TEXT, 'result')
        return result_link_elements

    def get_html_result_elements(self) ->list[WebElement]:
        result_link_element = self._driver.find_elements(By.LINK_TEXT, 'result in html')
        return result_link_element
