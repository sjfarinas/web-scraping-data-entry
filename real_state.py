from bs4 import BeautifulSoup
import requests


class Zillow:
    def __init__(self):
        self.response = requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
                                     headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36", "Accept-Language": "en-US,en;q=0.9,es-NI;q=0.8,es;q=0.7"})
        self.search_tracker = self.response.text
        self.soup = BeautifulSoup(self.search_tracker, "html.parser")
        self.homes_links = []
        self.home_prices = []
        self.home_addresses = []

    def get_urls(self):
        homes = self.soup.find_all(name="a", class_="list-card-img")
        for home in homes:
            if "http" not in home["href"]:
                self.homes_links.append(f"https://www.zillow.com{home['href']}")
            else:
                self.homes_links.append(home["href"])

    def get_prices(self):
        prices = self.soup.find_all(class_="list-card-price")
        self.home_prices = [price_tag.getText().split("+")[0].split("/mo")[0] for price_tag in prices]

    def get_addresses(self):
        addresses = self.soup.find_all(name="address", class_="list-card-addr")
        self.home_addresses = [address_tag.getText() for address_tag in addresses]