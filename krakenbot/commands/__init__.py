import click


def print_table_row(row=[], row_format=None, **kwargs):
    if not row_format:
        row_format = ''.join(['{: <20}' for item in row])
    click.secho(row_format.format(*row), **kwargs)
