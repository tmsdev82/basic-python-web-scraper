import click
from datetime import datetime, timezone
import json
import os
import requests

from bs4 import BeautifulSoup


@click.command()
@click.argument("urls", nargs=-1)
@click.option(
    "--output", default="data.json", help="The file to save the scraped data to."
)
def scrape_data_to_file(urls, output):
    scraped_data = []

    if os.path.exists(output):
        with open(output, "r") as file:
            scraped_data = json.load(file)

    for url in urls:
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")

        parent_div = soup.find("div", {"data-testid": "quote-statistics"})
        if not parent_div:
            print(f"No statistics div found for URL: {url}")
            continue

        stats_ul = parent_div.find("ul")
        if not stats_ul:
            print(f"No statistics found for URL: {url}")
            continue

        list_items = stats_ul.find_all("li")
        data = {}
        for item in list_items:
            columns = item.find_all("span")
            data[columns[0].get_text()] = columns[1].get_text()

        data["timestamp"] = str(datetime.now(timezone.utc))
        data["url"] = url
        data["ticker"] = url.split("/")[-1]
        print(json.dumps(data, indent=2))

        scraped_data.append(data)

    with open(output, "w") as file:
        json.dump(scraped_data, file, indent=2)


if __name__ == "__main__":
    scrape_data_to_file()
