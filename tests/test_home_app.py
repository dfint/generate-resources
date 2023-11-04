import pytest
from streamlit.testing.v1 import AppTest

import download_source
from download_source import ReleaseInfo


@pytest.fixture
def apptest(monkeypatch):
    def mock_get_latest_release():
        return ReleaseInfo(
            "Release Name",
            "classic/file.zip",
            "small/file.zip",
            "linux/file.tar.gz",
        )

    def mock_download_file(url: str, file_name: str):
        pass

    monkeypatch.setattr(download_source, "get_latest_release", mock_get_latest_release)
    monkeypatch.setattr(download_source, "download_file", mock_download_file)

    apptest = AppTest.from_file("Home.py")
    apptest.run()
    return apptest


def test_smoketest(apptest):
    assert not apptest.exception
