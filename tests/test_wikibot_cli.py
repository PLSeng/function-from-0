from mylib.bot import scrape
from click.testing import CliRunner
from wikibot_cli import main

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")
    
def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(main, ['--name', 'Microsoft', '--sentences', '5'])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output