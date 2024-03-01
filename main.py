import os
import time

import schedule

from telegram import TelegramBot
from tracker import MorningstarFetcher

bot_token = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']
stocks = {"F0GBR06PBI": "Fidelity - Emerging Market",
          "F00000VKNA": "Fidelity - Global Technology",
          "F00000W42B": "Fidelity - Global Dividend",
          "FOGBR05KLW": "Fidelity - Sustainable Health",
          "F00001654D": "Eurizon - Global Leaders ESG",
          "F000014HOD": "Eurizon - Equity Planet",
          "F000002A1J": "Vontobel - Global Environmental", }


def fetch_assets_type():
    fetcher = MorningstarFetcher(stocks)
    assets_type = {}
    assets_type["24h"] = fetcher.fetch_24h_change_rates()
    # assets_type["1 week"] = fetcher.fetch_1_week()
    assets_type["1 month"] = fetcher.fetch_1_month()
    # assets_type["3 month"] = fetcher.fetch_3_month()
    # assets_type["6 month"] = fetcher.fetch_6_month()
    assets_type["Year to date"] = fetcher.fetch_year_to_date()
    assets_type["1 year"] = fetcher.fetch_1_year()
    # assets_type["3 year"] = fetcher.fetch_3_year()
    # assets_type["5 year"] = fetcher.fetch_5_year()
    # assets_type["10 year"] = fetcher.fetch_10_year()
    return assets_type


def build_telegram_message(assets_type):
    message = "<b>Stock Asset Tracker</b> \n"
    for key, assets in assets_type.items():
        message += "\n \n <b>" + key + "</b> \n"
        for asset in assets:
            message = message + " \n " + asset.get_name() + ": <b>" + asset.get_change_rate() + "% </b>"
    return message


def send_telegram_message(message):
    telegram_bot = TelegramBot(bot_token, chat_id)
    telegram_bot.send_message(message)


def fetch_and_send():
    assets_type = fetch_assets_type()
    message = build_telegram_message(assets_type)
    send_telegram_message(message)


if __name__ == "__main__":
    print("Stock Asset Tracker running ... :)")

schedule.every().day.at("09:00").do(fetch_and_send)
# schedule.every(3).seconds.do(fetch_and_send)

while True:
    schedule.run_pending()
    time.sleep(1)
