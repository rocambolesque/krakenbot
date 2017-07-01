import click

from krakenbot.commands import print_table_row
from krakenbot.constants import ROUND_PRECISION
from krakenbot.models.trades_history import TradesHistory as TradesHistoryModel


class TradesBalance:
    def run():
        trades_history = TradesHistoryModel()

        head = [
            'Crypto currency',
            'Trades balance',
            'Volume',
            'Cost',
            'Value',
            'Profit',
        ]
        print_table_row(head, bold=True)
        for pair, trades in trades_history.trades:
            current_investment_value = trades.get_current_investment_value()
            profit = round(current_investment_value - trades.current_investment['vol'] * trades.current_investment['cost'], ROUND_PRECISION)
            row = [
                pair.crypto,
                trades.balance,
                trades.current_investment['vol'],
                trades.current_investment['cost'],
                current_investment_value,
                profit,
            ]
            print_table_row(row)
