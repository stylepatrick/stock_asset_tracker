import requests
from bs4 import BeautifulSoup

from tracker.Asset import Asset


class MorningstarFetcher:
    def __init__(self, stocks):
        self.__base_url_morningstar = "https://www.morningstar.it/it/funds/snapshot/snapshot.aspx?id="
        self.__stocks = stocks
        self.__html_sites = {}
        self.fetch()

    def fetch(self):
        self.__html_sites = {}
        for stock, name in self.__stocks.items():
            r = requests.get(self.__base_url_morningstar + stock + "&tab=1")
            soup = BeautifulSoup(r.text, "html.parser")
            self.__html_sites[stock] = soup

    def fetch_24h_change_rates(self):
        print("Fetching 24h change rates...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 2)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_1_week(self):
        print("Fetching 1 week changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 3)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_1_month(self):
        print("Fetching 1 month changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 4)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_3_month(self):
        print("Fetching 3 month changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 5)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_6_month(self):
        print("Fetching 6 month changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 6)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_year_to_date(self):
        print("Fetching year to date changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 7)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_1_year(self):
        print("Fetching 1 year changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 8)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_3_year(self):
        print("Fetching 3 year changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 9)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_5_year(self):
        print("Fetching 5 year changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 10)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def fetch_10_year(self):
        print("Fetching 10 year changes...")
        change_rates = []
        for stock, name in self.__stocks.items():
            change_rate = self.__collect_change_rate(self.__html_sites[stock], 11)
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates

    def __collect_change_rate(self, html_site, element):
        div = html_site.select_one("#returnsTrailingDiv")
        tr = div.select("tr")[element]
        change_rate = tr.select_one(".value").text.strip()
        print(change_rate)
        return change_rate.replace(",", ".")
