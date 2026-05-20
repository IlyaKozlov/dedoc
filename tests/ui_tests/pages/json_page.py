from selenium.webdriver.common.by import By

from ui_tests.pages.page_abc import Page


class JsonPage(Page):

    def get_json(self):
        xpath = '/html/body/pre'
        element = self._driver.find_element(By.XPATH, xpath)
        check_json = element.text
        return check_json