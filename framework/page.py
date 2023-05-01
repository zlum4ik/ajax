from time import sleep
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def element(self, locator):

        method = locator[0]
        values = locator[1]

        if type(values) is str:
            return self.find_element(method, values)
        elif type(values) is list:
            for value in values:
                try:
                    return self.find_element(method, value)
                except NoSuchElementException:
                    pass
            raise NoSuchElementException

    def find_element(self, method, value):
        if method == 'accessibility_id':
            return self.driver.find_element_by_accessibility_id(value)
        elif method == 'class_name':
            return self.driver.find_element_by_class_name(value)
        elif method == 'id':
            return self.driver.find_element_by_id(value)
        elif method == 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif method == 'name':
            return self.driver.find_element_by_name(value)
        else:
            raise Exception('Invalid locator method.')

    def wait_elements(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.element(locator)

    def click(self, locator):
        element = self.wait_elements(locator)
        element.click()

    def tap(self, locator):
        element = self.wait_elements(locator)
        element.tap()

    def send_keys(self, locator, text):
        element = self.wait_elements(locator)
        element.send_keys(text)
        sleep(0.5)

    def get_element(self, locator):
        element = self.wait_elements(locator)
        return element
