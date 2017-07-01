import click

from krakenbot.commands import print_table_row
from krakenbot.constants import ROUND_PRECISION
from krakenbot.models.balance import Balance as BalanceModel


class Balance:
    def run():
        balance = BalanceModel()

        head = [
            'Currency',
            'Balance',
        ]
        print_table_row(head, bold=True)
        for asset, asset_balance in balance.items:
            row = [
                asset.currency,
                asset_balance,
            ]
            print_table_row(row)
