from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import patch

import pytest
from streamlit.testing.v1 import AppTest

from download_source import ReleaseInfo

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


@pytest.fixture
@patch("download_source.download_file")
@patch("download_source.get_latest_release")
def apptest(get_latest_release: Callable[[], ReleaseInfo], download_file: Callable[[Path | str, str], None]):
    get_latest_release.return_value = ReleaseInfo(
        "Release Name",
        "classic/file.zip",
        "small/file.zip",
        "linux/file.tar.bz2",
    )

    download_file.return_value = None

    return AppTest.from_file("Home.py").run()


def test_smoketest(apptest: AppTest):
    assert not apptest.exception, apptest.exception[0].stack_trace
