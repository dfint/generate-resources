from pathlib import Path

import pytest

from download_source import ReleaseInfo, base_url, parse_download_info

tests_dir = Path(__file__).parent


@pytest.fixture
def downloads_page():
    with open(tests_dir / "assets" / "downloads.html") as file:
        yield file.read()


def test_parse_downloads_page(downloads_page):
    result = parse_download_info(downloads_page)
    assert result == ReleaseInfo(
        name="DF 50.11 (October 3, 2023)",
        classic_win_url=base_url + "df_50_11_win.zip",
        classic_win_small_url=base_url + "df_50_11_win_s.zip",
        linux_url=base_url + "df_50_11_linux.tar.bz2",
    )
