from os import listdir
import logging
from pprint import pformat
from app.main import fb


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# requests_mock.get('http://fb.me', json=header)
# mocked_request = requests.get('http://fb.me')


def test_check_header_fbme(header_w_attach: dict) -> None:
    test_filename = header_w_attach['Content-Disposition'].split('=')[1]
    assert test_filename == fb.check_header(header_w_attach)


def test_check_header_fbme_wrong_filetype(header_w_attach: dict) -> None:
    header_w_attach['Content-Disposition'] = 'other-file.wav'
    assert fb.check_header(header_w_attach) is None
    header_w_attach['Content-Disposition'] = 'no-extension-file'
    assert fb.check_header(header_w_attach) is None
    header_w_attach['Content-Disposition'] = 'special-chars-?>#@'
    assert fb.check_header(header_w_attach) is None


def test_save_audio_fbme(audioclip: bytes) -> None:
    # header_w_attach['Content-Disposition'] = 'other-file.wav'
    # assert fb.check_header(header_w_attach) is None
    fb.save_audio(audioclip, 'audioclip.mp4')
    temp_folder = getenv('TEMP_FOLDER')
    temp_index = listdir(temp_folder).index('audioclip.mp4')
    



    pass