
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Browser():

    def __init__(self, selenium_driver, wait_interval=10):
        self.selenium_driver = selenium_driver
        self.wait_interval = wait_interval

    def open_page(self, url):
        self.selenium_driver.get(url)

    def click_on_element(self, locator_type, locator):
        element = self.get_enabled_element(locator_type, locator)
        element.click()

    def type_to_text_field(self, locator_type, locator, value):
        element = self.get_enabled_element(locator_type, locator)
        element.send_keys(value)

    def close(self):
        self.selenium_driver.quit()

    def get_element(self, locator_type, locator):
        wait = WebDriverWait(self.selenium_driver, self.wait_interval)
        wait.until(lambda x: self.find_element(
            locator_type, locator) is not None)
        element = self.find_element(locator_type, locator)
        return element

    def get_enabled_element(self, locator_type, locator):
        wait = WebDriverWait(self.selenium_driver, self.wait_interval)
        wait.until(lambda x: self.check_element_is_displayed(
            locator_type, locator))
        wait.until(lambda x: self.check_element_is_enabled(
            locator_type, locator))
        element = self.find_element(locator_type, locator)
        return element

    def find_element(self, locator_type, locator):
        try:
            element = self.selenium_driver.find_element(
                locator_type, locator)
        except Exception as exc:
            element = None
        return element

    def check_element_is_displayed(self, locator_type, locator):
        try:
            result = self.find_element(
                locator_type, locator).is_displayed()
        except Exception as exc:
            result = False
        return result

    def check_element_is_enabled(self, locator_type, locator):
        try:
            result = self.find_element(
                locator_type, locator).is_enabled()
        except Exception as exc:
            result = False
        return result

