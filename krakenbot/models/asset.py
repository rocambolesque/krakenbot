class Asset:
    def __init__(self, asset):
        self.asset = asset

    @property
    def currency(self):
        return self.asset[1:]
