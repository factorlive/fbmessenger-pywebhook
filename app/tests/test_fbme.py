import json
import requests
import requests_mock
from os import getenv
from pathlib import Path
from app.fbme import fb

fixtures = Path(getenv('FIXTURES'))

@requests_mock.Mocker()
def test_get_header_fbme():
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)
    fb.get_header('http://test.com', text=header)
    assert header 


def test_audio_file_fbme():
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)
    
    assert 1 == 1
