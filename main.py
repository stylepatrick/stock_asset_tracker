from tracker import MorningstarFetcher
from telegram import TelegramBot
import schedule
import time
import os

bot_token = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']
stocks = {"F0GBR06PBI": "Fidelity - Emerging Market",
          "F00000VKNA": "Fidelity - Global Technology",
          "F00000W42B": "Fidelity - Global Dividend",
          "FOGBR05KLW": "Fidelity - Sustainable Health",
          "F00001654D": "Eurizon - Global Leaders ESG",
          "F000014HOD": "Eurizon - Equity Planet",
          "F000002A1J": "Vontobel - Global Environmental", }


def fetch_morningstar():
    fetcher = MorningstarFetcher(stocks)
    change_rates = fetcher.fetch_24h_change_rates()
    return change_rates


def send_telegram_message(change_rates):
    telegram_bot = TelegramBot(bot_token, chat_id)
    telegram_bot.send_message(change_rates)


def fetch_and_send():
    assets = fetch_morningstar()
    send_telegram_message(assets)


if __name__ == "__main__":
    print("Stock Asset Tracker running ... :)")

schedule.every().day.at("09:00").do(fetch_and_send)
# schedule.every(3).seconds.do(fetch_and_send)

while True:
    schedule.run_pending()
    time.sleep(1)
