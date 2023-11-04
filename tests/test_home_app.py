from unittest.mock import patch

import pytest
from streamlit.testing.v1 import AppTest

from download_source import ReleaseInfo


@pytest.fixture
@patch("download_source.download_file")
@patch("download_source.get_latest_release")
def apptest(get_latest_release, download_file):
    get_latest_release.return_value = ReleaseInfo(
            "Release Name",
            "classic/file.zip",
            "small/file.zip",
            "linux/file.tar.bz2",
        )
    
    download_file.return_value = None
    
    apptest = AppTest.from_file("Home.py")
    apptest.run()
    return apptest


def test_smoketest(apptest):
    assert not apptest.exception, apptest.exception[0].stack_trace
