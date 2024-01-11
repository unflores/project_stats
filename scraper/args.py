from argparse import ArgumentParser
import pkgutil


def parse_args(args):
    return _parser.parse_args(args=args)


def help_text():
    """This exists primarily to test the help text integration :|"""

    return _parser.format_help()


def _possible_processors():
    """All the processors will be a module within the processors dpackage"""
    return [name for _, name, _ in pkgutil.iter_modules(['./scraper/processors'])]


_parser = ArgumentParser(
    description='Scrape some project statistics', exit_on_error=False
)
_parser.add_argument(
    '--processor',
    help='Possible processors for scraping project. ex={}'.format(
        ', '.join(_possible_processors())
    ),
)
