class Asset:
    def __init__(self, asset):
        self.asset = asset

    @property
    def currency(self):
        if self.asset[0] == 'X':
            return self.asset[1:]
        if self.asset[0] == 'Z':
            return self.asset[1:]
        return self.asset
