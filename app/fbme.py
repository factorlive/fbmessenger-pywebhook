from typing import Optional
import hmac
import hashlib
from os import getenv, remove
from pathlib import Path
import requests
import logging

# Logging toolbox 🔊
# TODO clean up logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FBME_API_HOST = getenv('FBME_API_HOST', 'fbme_api_host_missing')
FBME_API_VERSION = getenv('FBME_API_VERSION', 'fbme_api_version_missing')


class Messenger(object):
    def __init__(self):
        self.session = requests.Session()
        self.app_secret = getenv('FB_APP_SECRET', 'missing_secret')

    def credentials(self) -> str:
        params = {}
        app_secret = getenv('FB_APP_SECRET', 'missing_secret').encode()
        params['access_token'] = getenv(
            'FB_PAGE_ACCESS_TOKEN', 'missing_page_access_token').encode()
        params['appsecret_proof'] = hmac.new(app_secret, access_token, hashlib.sha256).hexdigest()
        return (f'?access_token={getenv("FB_PAGE_ACCESS_TOKEN")}'
                f'?appsecret_proof={appsecret_proof}')

    def message(self, recipient: int, message: str) -> dict:
        message_body = {
            'recipient': {'id': recipient},
            'message': {'text': message}
        }
        gateway = FBME_API_HOST + '/' + FBME_API_VERSION + '/me/messages'
        # access_token = f'?access_token={getenv("FB_PAGE_ACCESS_TOKEN")}'
        response = requests.post(gateway + self.credentials(), params=message_body).json()
        logger.info(response)
        return response

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
