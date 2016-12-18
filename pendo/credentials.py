__author__ = 'dmitry_boyko'

class GooglePage():

    def open(self):
        return {
            "google_url": "https://www.google.com/",
            "yahoo_url":  "https://www.yahoo.com/"
            }

    def search(self):
        return {
            "h_sack": "hacky sack",                 # string
            "search_fld": "lst-ib",                 # by ID
            "search_icon": "_fZl",                  # by  ID
            "shopping": "a.q.qs",                   # by CSS
            "shopping_t": "Shopping"                # by Link_Text
            }

    def save_to_shop_list(self):
        return {
            "g4": "//div[4]/div/h3/a",              # by xpath:position
            "addToList": "//div[4]/div[2]/div",     # by xpath
            "save": "div.gko-a-lbl",                # by CSS
            "note": "Please buy me"                 # string
            }

