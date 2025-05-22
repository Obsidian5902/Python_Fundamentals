class webBrowser:
    connected = True # class attribute
    counter_web_browser = 0 # class variable/ attribute

    def __init__(self, page):
        self.history = [page]
        self.current_page = page
        self.is_incognito = False
        webBrowser.counter_web_browser += 1

print(webBrowser.counter_web_browser)
chrome = webBrowser("Tumbler.com")
firefox = webBrowser("Google.com")
print(webBrowser.counter_web_browser)
onion = webBrowser("onion.com")
print(webBrowser.counter_web_browser)