import pytest
from os import getenv
import json
from pathlib import Path

fixtures = Path(getenv('FIXTURES'))


@pytest.fixture(scope="module")
def header_w_attach() -> dict:
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)
    return header
