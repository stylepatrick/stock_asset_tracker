import requests
from bs4 import BeautifulSoup

from tracker.Asset import Asset


class MorningstarFetcher:
    def __init__(self, stocks):
        self.__base_url_morningstar = "https://www.morningstar.it/it/funds/snapshot/snapshot.aspx?id="
        self.__stocks = stocks

    def fetch_24h_change_rates(self):
        change_rates = []
        for stock, name in self.__stocks.items():
            r = requests.get(self.__base_url_morningstar + stock)
            soup = BeautifulSoup(r.text, "html.parser")
            div = soup.select_one("#overviewQuickstatsDiv")
            tr = div.select("tr")[2]
            change_rate = tr.select_one(".text").text.strip()[:-1]
            change_rate = change_rate.replace(",", ".")
            change_rates.append(Asset(stock, name, change_rate))
        return change_rates
