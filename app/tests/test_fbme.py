import logging
from pprint import pformat
import json
import requests
from os import getenv
from pathlib import Path
from app.main import fb

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
    # requests_mock.get('http://fb.me', json=header)
    # mocked_request = requests.get('http://fb.me')


def test_check_header_fbme():
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)
    # logger.info(fb.check_header(mocked_request))
    logger.info(pformat(header, depth=2))
    test_filename = header['Content-Disposition'].split('=')[1]
    assert test_filename == fb.check_header(header)
    header['Content-Disposition'] = 'other-file.wav'
    test_filename = header['Content-Disposition']
    filename = fb.check_header(header)
    logger.info(test_filename)
    logger.info(filename)
    assert fb.check_header(header) == False

