import click
import sys
from template_package.utils import iter_together


@click.command()
@click.argument('left')
@click.argument('right')
@click.option('--output', default=sys.stdout, type=click.File('w'))
def main(left, right, output):
    results = iter_together(left, right)
    for a, b in results:
        print(a, b, file=output
              )

if __name__ == '__main__':
    # Run out Cli
    main()