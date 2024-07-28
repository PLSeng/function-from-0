import click
from wikibot import scrape


@click.command()
@click.option("--name", default="Microsoft", help="The name of the article to scrape.")
@click.option("--sentences", default=2, help="The number of sentences to scrape.")
def main(name, sentences):
    click.echo(click.style(f"{scrape(name, sentences)}", fg="green"))


if __name__ == "__main__":
    main()

# Run the script with the following command:
# python wikibot_cli.py --name "Microsoft" --sentences 3
