from real_state import Zillow
from google_form import GoogleForm

zillow_scrapping = Zillow()
zillow_scrapping.get_urls()
zillow_scrapping.get_prices()
zillow_scrapping.get_addresses()

google_form = GoogleForm()
google_form.fill_form(addresses=zillow_scrapping.home_addresses,
                      prices=zillow_scrapping.home_prices,
                      links=zillow_scrapping.homes_links)
