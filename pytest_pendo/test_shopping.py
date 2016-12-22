
import os
import pytest
import time
from browser import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from page_google import PageGoogle


def test_save_item_to_shortlist(browser):
    page_google = PageGoogle(browser)
    page_google.open()
    page_google.search('hacky sack')
    page_google.search(Keys.ESCAPE)
    page_google.go_to_shopping()
    page_google.save_item_to_shortlist(4)
    time.sleep(3)


@pytest.fixture(scope='session')
def browser(request):
    #browser = Browser(webdriver.Firefox())
    browser = Browser(webdriver.Chrome())
    def browser_close():
        browser.close()
    request.addfinalizer(browser_close)
    return browser


def main():
    pytest.main(['-s', '-v', os.path.basename(__file__)])


if __name__ == '__main__':
    main()
