import click
from .fetch import get_contributing_md


def main(output):
    contributing_md = get_contributing_md()
    with open(output, 'w+') as f:
        f.write(contributing_md)

@click.command()
@click.option('-o', '--output', required=False, default='CONTRIBUTING.md')
def cli(*args, **kwargs):
    main(*args, **kwargs)


if __name__ == "__main__":
    cli()
