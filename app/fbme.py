from typing import Optional
from os import getenv
from pathlib import Path
import logging

# Logging toolbox 🔊
# TODO clean up logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Messenger(object):
    def check_header(self, header: dict) -> Optional[str]:
        audio_file = str(header.get('Content-Disposition'))
        if 'mp4' not in audio_file.split('.'):
            return None
        return audio_file.split('=')[1]

    def save_audio(self, audioclip, filename):
        temp_folder = Path(getenv('TEMP_FOLDER'))
        temp_file = temp_folder / filename
        with open(temp_file, 'wb') as f:
            f.write(audioclip)
        return 'save audio says file saved'


fb = Messenger()
