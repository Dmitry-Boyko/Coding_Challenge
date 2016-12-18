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
            "shopping": "a.q.qs",                   # by CSS
            "shopping_t": "Shopping"                # by Link_Text
            }

    def save_to_shop_list(self):
        return {
            "g4": "//div[4]/div/div/a/div/img",     # by xpath:position  //div[4]/div/h3/a
            "addToList": "//div[@id='rso']/div//div[7]/div/div[2]//div[2]/div[3]/div[4]/div[2]/div",     # by xpath  "//div[4]/div[2]/div"
            "save": "div.gko-a-lbl",                # by CSS
            "note": "Please buy me"                 # string
            }

