from importlib.resources import path

from ui_tests.ui_tests_abc import UiTests
from selenium.webdriver.common.by import By

class TestReturnFormats(UiTests):
    def chose_formats(self):
        xpath = '/html/body/form/div[1]/details/p[5]/label/select'
        chose_format = self.driver.find_element(By.XPATH, xpath)
        return chose_format

    def test_return_formats_click(self):
        self.chose_formats()
        html_xpath ='/html/body/form/div[1]/details/p[5]/label/select/option[1]'
        self._click_element(html_xpath)
        p_json_xpath = '/html/body/form/div[1]/details/p[5]/label/select/option[2]'
        self._click_element(p_json_xpath)
        text_xpath = '/html/body/form/div[1]/details/p[5]/label/select/option[3]'
        self._click_element(text_xpath)
        tree_xpath = '/html/body/form/div[1]/details/p[5]/label/select/option[4]'
        self._click_element(tree_xpath)
        json_xpath = '/html/body/form/div[1]/details/p[5]/label/select/option[5]'
        self._click_element(json_xpath)
        c_tree = '/html/body/form/div[1]/details/p[5]/label/select/option[6]'
        self._click_element(c_tree)

    def _click_element(self, xpath: str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def test_return_formats(self):
        self.chose_formats()
        from form in self.test_return_formats_click(xpath)
        self.main_page.choose_file(path)
        self.main_page.upload_file(path)




