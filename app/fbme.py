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
        audio_file = header.get('filename')
        if 'mp4' in audio_file.split('.'):
            return audio_file
        return False


fb = Messenger()
