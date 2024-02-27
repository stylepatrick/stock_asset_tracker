import requests


class TelegramBot:

    def __init__(self, bot_token, chat_id):
        self.__base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=html&text="

    def send_message(self, assets):
        message = "<b>Stock Asset Tracker</b>%0A"
        for asset in assets:
            message = message + "%0A" + asset.get_name() + ": <b>" + asset.get_change_rate() + " % </b>"
        url = self.__base_url + message
        # print(url)
        requests.get(url).json()
