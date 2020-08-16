import requests
import logging

# Logging toolbox 🔊
# TODO clean up logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("song")


class Song():
    def log_song(self, url):
        logger.info(url)


song = Song()
