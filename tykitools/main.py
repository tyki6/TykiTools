import click

from tykitools.scripts.ip_lookup import ip_lookup_from_string


@click.group()
def cli() -> None:
    """CLI Tool"""
    pass


@click.command()
@click.argument("ip")
def iplookup(ip: str) -> None:
    """Lookup IP Address"""
    print(ip_lookup_from_string(ip))


cli.add_command(iplookup)
if __name__ == "__main__":
    cli()
