import json
from os import getenv
from pathlib import Path
from app.fbme import fb

fixtures = Path(getenv('FIXTURES'))


def test_audio_file_fbme():
    h = fixtures / 'header_w_attach.json'
    with open(h, 'r') as f:
        header = json.load(f)
    
    assert 1 == 1