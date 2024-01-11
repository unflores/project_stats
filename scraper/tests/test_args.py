from scraper.args import parse_args, help_text


def test_parse_args_provides_help_examples():
    assert 'release_candidate' in help_text()


def test_parse_args_returns_proper_processor():
    assert (
        'release_candidate'
        == parse_args(args=['--processor=release_candidate']).processor
    )
