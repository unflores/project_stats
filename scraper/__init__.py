from argparse import ArgumentParser
import pkgutil


def build_parser():
    parser = ArgumentParser(description='Scrape some project statistics')
    parser.add_argument(
        '--processor',
        help='Possible processors for scraping project. ex={}'.format(
            ', '.join(_possible_processors())
        ),
    )
    return parser


def _possible_processors():
    return [name for _, name, _ in pkgutil.iter_modules(['./scraper/processors'])]
