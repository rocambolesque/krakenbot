from krakenbot.api import api_client
from krakenbot.models.pair import Pair
from krakenbot.models.trades import Trades

class TradesHistory:
    history = {}

    def __init__(self):
        self.fetch_trades()

    def fetch_trades(self):
        response = api_client.query_private('TradesHistory')

        # split trades by type (buy/sell) and currency
        for key, trade in response['result']['trades'].items():
            if not self.history.get(trade['pair']):
                self.history[trade['pair']] = {}
            if not self.history[trade['pair']].get(trade['type']):
                self.history[trade['pair']][trade['type']] = []
            self.history[trade['pair']][trade['type']].append(trade)

    @property
    def trades(self):
        for pair_key, pair_trades in self.history.items():
            pair = Pair(pair_key)
            trades = Trades(pair, pair_trades)
            yield pair, trades
