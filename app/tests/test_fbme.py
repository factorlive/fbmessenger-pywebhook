import logging
from pprint import pformat
import json
import requests
from os import getenv
from app.main import fb


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

    # requests_mock.get('http://fb.me', json=header)
    # mocked_request = requests.get('http://fb.me')


def test_check_header_fbme(header_w_attach) -> None:
    test_filename = header_w_attach['Content-Disposition'].split('=')[1]
    assert test_filename == fb.check_header(header_w_attach)

def test_check_header_fbme_wrong_filetype(header_w_attach):
    header_w_attach['Content-Disposition'] = 'other-file.wav'
    assert fb.check_header(header_w_attach) is None

