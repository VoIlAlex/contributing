from .fetch import get_contributing_md
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--output',
        help="output file. Don't care, just use default.",
        required=False,
        default='CONTRIBUTING.md'
    )
    args = parser.parse_args()
    return args


def cli():
    args = parse_args()
    contributing_md = get_contributing_md()
    with open(args.output, 'w+') as f:
        f.write(contributing_md)


if __name__ == "__main__":
    cli()
