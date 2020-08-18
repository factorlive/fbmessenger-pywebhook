from typing import Optional
from os import getenv, remove
from pathlib import Path
import logging

# Logging toolbox 🔊
# TODO clean up logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Messenger(object):
    def message(self, params: dict):

    def check_header(self, header: dict) -> Optional[str]:
        audio_file = header.get('Content-Disposition', 'no_audio_file')
        if 'mp4' not in audio_file.split('.'):
            return None
        return audio_file.split('=')[1]

    def save_audio(self, audioclip: bytes, audioclip_name: str) -> None:
        temp_folder = Path(getenv('TEMP_FOLDER', default='missing_temp_env_path'))
        temp_file = temp_folder / audioclip_name
        with open(temp_file, 'wb') as f:
            f.write(audioclip)
        return None

    def remove_audio(self, audioclip_name: str) -> None:
        temp_folder = Path(getenv('TEMP_FOLDER', default='missing_temp_env_path'))
        temp_file = temp_folder / audioclip_name
        return remove(temp_file)


fb = Messenger()
