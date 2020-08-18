import pytest
from os import getenv
import json
from pathlib import Path

fixtures = Path(getenv('FIXTURES', default='missing_fixtures_folder'))


@pytest.fixture(scope="module")
def post_msg_response() -> dict:
    h = fixtures / 'post_msg_response.json'
    with open(h, 'r') as f:
        header = json.load(f)
    return header


@pytest.fixture(scope="module")
def header_w_attach() -> dict:
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)
    return header


@pytest.fixture(scope="module")
def audioclip() -> bytes:
    fix = fixtures / 'audioclip.mp4'
    with open(fix, 'rb') as f:
        audio = f.read()
    return audio


@pytest.fixture(scope="module")
def audioclip_name() -> str:
    return 'audioclip.mp4'
