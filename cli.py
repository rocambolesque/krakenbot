import click

from krakenbot.commands.trades_balance import TradesBalance
from krakenbot.commands.balance import Balance


@click.group()
def cli():
    pass


@click.command('trades-balance')
def trades_balance():
    TradesBalance.run()


@click.command('balance')
def balance():
    Balance.run()

cli.add_command(trades_balance)
cli.add_command(balance)


if __name__ == '__main__':
    cli()
