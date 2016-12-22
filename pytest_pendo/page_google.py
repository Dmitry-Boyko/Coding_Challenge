
from selenium.webdriver.common.by import By


class PageGoogle():

    URL = 'https://www.google.com'

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        # Open Google page
        self.browser.open_page(self.URL)

    def search(self, term):
        # Type to "search" field
        self.browser.type_to_text_field(
            locator_type=By.ID,
            locator='lst-ib',
            value=term
        )

    def go_to_shopping(self):
        # Click on "Shopping" link
        self.browser.click_on_element(
            locator_type=By.CSS_SELECTOR,
            locator='a.q.qs',
        )

    def save_item_to_shortlist(self, number):
        # Waiting for content to load
        self.browser.get_enabled_element(
            locator_type=By.XPATH,
            locator='//div[@id=\'rso\']/div/div/div[{}]/div/div[2]/div/span/b'.format(number),
        )
        # Click on "number"-th item in the list
        self.browser.click_on_element(
            locator_type=By.XPATH,
            locator='//div[@id=\'rso\']/div/div/div[{}]/div/h3/a'.format(number),
        )
        # Waiting for content to load
        self.browser.get_enabled_element(
            locator_type=By.XPATH,
            locator='//div[@id=\'rso\']/div/div/div[{}]/div/div[2]/div/span/b'.format(number),
        )
        # Click on "Save to Shortlist" button
        self.browser.click_on_element(
            locator_type=By.CSS_SELECTOR,
            locator='div.gko-a-lbl',
        )
