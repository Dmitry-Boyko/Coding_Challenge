__author__ = 'dmitry_boyko'

"""
1. open
2. search(search_term)
3. save_to_shop_list(item_number, note)

google_page = GooglePage(selenium_driver)
google_page.open()
google_page.search("hacky sack")
google_page.shopping_page("hacky sacks")
google_page.save_to_shop_list(4, "Please buy me")
"""

import sys
from selenium                           import webdriver
from selenium.webdriver.common.by       import By
from credentials                        import GooglePage
from selenium.webdriver.common.keys     import Keys

from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC


def driver():
    selenium_driver = webdriver.Chrome()
    #selenium_driver = webdriver.Firefox()
    selenium_driver.set_page_load_timeout(30)
    selenium_driver.implicitly_wait(30)
    selenium_driver.maximize_window()
    return selenium_driver

def main():
    d = driver()
    browse = BrowseAndBuy()
    browse.open_browser(d)
    browse.search_item(d)
    browse.shopping_page(d)
    browse.save_to_shop_list(d)
    d.quit()


class BrowseAndBuy():
    def open_browser(self, selenium_driver):
        gp = GooglePage()
        selenium_driver.get(gp.open()["google_url"])

    def search_item(self, selenium_driver):
        gp = GooglePage()
        selenium_driver.find_element(By.ID, gp.search()["search_fld"]).send_keys(gp.search()["h_sack"])
        selenium_driver.find_element(By.ID, gp.search()["search_fld"]).send_keys(Keys.RETURN)


    def shopping_page(self, selenium_driver):
        gp = GooglePage()
        element = WebDriverWait(selenium_driver, 4).until(
            EC.presence_of_element_located((By.LINK_TEXT, gp.search()["shopping_t"]))
        )
        element.click()

    def save_to_shop_list(self, selenium_driver):
        gp = GooglePage()
        selenium_driver.find_element(By.XPATH, gp.save_to_shop_list()["g4"]).click()

        element_b = WebDriverWait(selenium_driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, gp.save_to_shop_list()["addToList"]))
        )
        element_b.click()
        print (gp.save_to_shop_list()["note"])

if __name__ == "__main__":
    main()