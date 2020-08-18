import logging
import json
import requests
import requests_mock
from os import getenv
from pathlib import Path
from app.fbme import fb

fixtures = Path(getenv('FIXTURES'))

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# @requests_mock.Mocker()
# def test_get_header_fbme():
#     h = fixtures / 'header_w_attach.json'
#     with open(h, 'r') as f:
#         header = json.load(f)
#     fb.get_header('http://test.com', text=header)
#     assert header 


def test_audio_file_fbme(requests_mock):
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)
    logger.info(header)
    assert 1 == 1
