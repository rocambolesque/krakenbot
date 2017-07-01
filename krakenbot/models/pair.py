class Pair:
    def __init__(self, pair):
        self.pair = pair

    def __str__(self):
        return self.pair

    @property
    def crypto(self):
        return self.pair[1:self.pair.find('Z')]

    @property
    def currency(self):
        return self.pair[self.pair.find('Z')+1:]
