from splinter.browser import Browser                   # importeer de Browser klasse
import logging

logformat="%(levelname)s:%(asctime)s:%(filename)s:%(lineno)d:%(message)s"
logging.basicConfig(filename='./example.log', level=logging.DEBUG, format=logformat)
logging.info("The program has started")

logging.debug("Setting browser")
browser = Browser('chrome')                            # instantieer een browser object

logging.debug("Opening website")
browser.visit("https://duckduckgo.com")                # laat de browser naar een URL navigeren

logging.debug("typing search command")
browser.fill('q', 'raspberry pi retro website')        # vul een zoektekst in

logging.debug("clicking on search")
button = browser.find_by_id('search_button_homepage')  # Zoek de Zoek knop
button.click()                                         # Druk op de knop

logging.info("quiting browser")
browser.quit()                                         # Sluit de browser