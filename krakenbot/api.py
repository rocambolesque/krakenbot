import os

import krakenex

api_client = krakenex.API()
api_client.load_key(os.getenv('KRAKEN_API_KEYFILE'))
