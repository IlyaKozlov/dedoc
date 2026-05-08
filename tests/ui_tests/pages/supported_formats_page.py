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
