from typing import NamedTuple

import requests
from bs4 import BeautifulSoup

base_url = "http://www.bay12games.com/dwarves/"


class ReleaseInfo(NamedTuple):
    name: str
    classic_win_url: str
    classic_win_small_url: str
    linux_url: str


def parse_download_info(page_content: bytes) -> ReleaseInfo:
    soup = BeautifulSoup(page_content, "html.parser")
    body = soup.body

    tables = body.select("table")
    release_table = tables[1]

    release_name = release_table.find("p").contents[0]

    links = dict()
    for link in release_table.select("a")[:3]:
        name = link.text.lower().partition(" ")[0]
        links[name] = base_url + link["href"]

    return ReleaseInfo(release_name, links["classic"], links["small"], links["linux"])


def get_latest_release() -> ReleaseInfo:
    """
    Get the latest release of Dwarf Fortress from the downloads page

    Returns:
        ReleaseInfo: information about the latest release
    """
    url = base_url + "older_versions.html"
    response = requests.get(url)
    response.raise_for_status()
    return parse_download_info(response.content)


if __name__ == "__main__":
    print(get_latest_release())
