class Pair:
    crypto = ''
    fiat = ''

    def __init__(self, pair):
        self.pair = pair
        self.set_assets(pair)

    def __str__(self):
        return self.pair

    def set_assets(self, pair):
        self.crypto = pair[:4]
        self.fiat = pair[4:]
        if self.crypto[0] == 'X':
            self.crypto = self.crypto[1:]
        if self.fiat[0] == 'Z':
            self.fiat = self.fiat[1:]
