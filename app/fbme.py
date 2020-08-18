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
        logger.info(header)
        audio_file = header.get('Content-Disposition')
        if 'mp4' not in audio_file.split('.'):
            return None
        filename = audio_file.split('=')[1] 
        return filename

    def save_audio(self, request, filename):
        temp_folder = Path(getenv('TEMP_FOLDER'))
        temp_file = temp_folder / filename
        with open(temp_file, 'wb') as f:
            f.write(request.content)
        return request.status_code


fb = Messenger()
