import click

from tykitools.scripts.ip_lookup import ip_lookup_from_string
from tykitools.scripts.social_media_lookup import social_media_lookup_by_username


@click.group()
def cli() -> None:
    """CLI Tool"""
    pass


@click.command()
@click.argument("ip")
def iplookup(ip: str) -> None:
    """Lookup IP Address"""
    print(ip_lookup_from_string(ip))


@click.command()
@click.argument("username")
def reseaux(username: str) -> None:
    """Lookup IP Address"""
    social_media_lookup_by_username(username)


cli.add_command(iplookup)
cli.add_command(reseaux)
if __name__ == "__main__":
    cli()
