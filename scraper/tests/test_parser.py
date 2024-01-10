from scraper import build_parser


def test_parser_provides_help_examples_from_modules():
    parser = build_parser()
    assert 'release_candidate' in parser.format_help()
