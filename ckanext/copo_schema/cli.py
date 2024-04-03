import click


@click.group(short_help="copo_schema CLI.")
def copo_schema():
    """copo_schema CLI.
    """
    pass


@copo_schema.command()
@click.argument("name", default="copo_schema")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [copo_schema]
