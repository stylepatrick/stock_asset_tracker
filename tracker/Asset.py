class Asset:
    def __init__(self, asset, name, change_rate):
        self.asset = asset
        self.name = name
        self.change_rate = change_rate

    def get_asset(self):
        return self.asset

    def get_name(self):
        return self.name

    def get_change_rate(self):
        return self.change_rate

    def __str__(self):
        return self.name + ": " + str(self.change_rate) + "%"
