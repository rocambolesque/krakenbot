from krakenbot.api import api_client
from krakenbot.models.asset import Asset


class Balance:
    def __init__(self):
        self.fetch_balance()

    def fetch_balance(self):
        response = api_client.query_private('Balance')
        self.balance = response['result']

    @property
    def items(self):
        for asset_key, asset_balance in self.balance.items():
            asset = Asset(asset_key)
            yield asset, asset_balance
