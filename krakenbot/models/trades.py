from operator import itemgetter

from krakenbot.api import api_client
from krakenbot.constants import BUY, ROUND_PRECISION, SELL, TRADE_TYPES
from krakenbot.models.spread import Spread


class Trades:
    def __init__(self, pair, trades):
        self.trades = trades
        self.pair = pair

        # order trades in chronological order
        for trade_type in {BUY, SELL}:
            if self.trades.get(trade_type):
                self.trades[trade_type] = sorted(self.trades[trade_type], key=itemgetter('time'), reverse=True)

        self.buys = self.trades.get(BUY, [])
        self.sells = self.trades.get(SELL, [])

        self.set_current_investment()
        self.set_trade_balance()

    def set_current_investment(self):
        self.sold_buys = []
        self.unsold_buys = []
        self.current_investment = {'vol': 0, 'cost': 0}

        if not self.buys:
            return

        if not self.sells:
            self.unsold_buys = self.buys
        else:
            i = 0
            while i < len(self.buys) and self.buys[i]['time'] > self.sells[0]['time']:
                i = i + 1
            self.sold_buys = self.buys[i:]
            self.unsold_buys = self.buys[:i]

        if self.unsold_buys:
            total_cost = 0
            for buy in self.unsold_buys:
                total_cost = total_cost + float(buy['cost'])
                self.current_investment['vol'] = self.current_investment['vol'] + float(buy['vol'])
            self.current_investment['cost'] = total_cost / self.current_investment['vol']

    def set_trade_balance(self):
        bought = sum(float(buy['cost']) for buy in self.sold_buys)
        sold = sum(float(sell['cost']) for sell in self.sells)
        if bought > 0 and sold == 0:  # one or more buys, no sells: money invested
            self.balance = 0
        else:
            self.balance = round(sold - bought, ROUND_PRECISION)

    def get_current_investment_value(self):
        spread = Spread(self.pair)
        current_investment_value = self.current_investment['vol'] * spread.last_average
        return current_investment_value
