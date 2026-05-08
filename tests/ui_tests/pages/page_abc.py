from abc import ABC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Page(ABC):
    def __init__(self, driver:WebDriver):
        self._driver = driver

    def wait_windows(self, timeout: float, tabs: list[str]) -> str:
        WebDriverWait(self._driver, timeout).until(lambda d: len(d.window_handles) > len(tabs))
        new_tabs = self._driver.window_handles
        new_tab = [tab for tab in new_tabs if tab not in tabs][0]
        return new_tab
