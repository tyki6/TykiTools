import click
from src.ip_lookup import ip_lookup

@click.group()
def cli():
    """CLI Tool"""
    pass

@click.command()
@click.argument("ip")
def iplookup(ip):
    """Lookup IP Address"""
    print(ip_lookup(ip))
    
cli.add_command(iplookup)
if __name__ == '__main__':
    cli()
