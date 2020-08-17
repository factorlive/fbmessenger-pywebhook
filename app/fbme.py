from os import getenv
from pathlib import Path
import requests
import logging

# Logging toolbox 🔊
# TODO clean up logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fbme")


class Messenger(object):
    def audio_file(self, url):
        h = requests.head(url, allow_redirects=True)
        header = h.headers
        logger.info(header)
        audio_file = header.get('Content-Disposition')
        if 'mp4' in audio_file.split('.'):
            return audio_file.split('=')[1]
        return False

    def save_audio(self, url, audio_file):
        r = requests.get(url)
        temp_folder = Path(getenv('TEMP_FOLDER'))
        temp_file = temp_folder / audio_file
        with open(temp_file, 'wb') as f:
            f.write(r.content)
        return r.status_code


fb = Messenger()
