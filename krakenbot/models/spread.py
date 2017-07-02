from krakenbot.api import api_client
from krakenbot.constants import ROUND_PRECISION


class Spread:
    def __init__(self, pair):
        self.pair = pair
        self.fetch_spread()

    def fetch_spread(self):
        response = api_client.query_public('Spread', {'pair': '{}{}'.format(self.pair.crypto, self.pair.fiat)})
        self.spread = response['result'][str(self.pair)]

    @property
    def last_average(self):
        last_spread = self.spread[-1]
        spread_min = round(float(last_spread[1]), ROUND_PRECISION)
        spread_max = round(float(last_spread[2]), ROUND_PRECISION)
        average = (spread_min + spread_max) / 2  # average value (min+max)/2
        return average
