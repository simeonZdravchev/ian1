import os
import signal
import subprocess
import re
import logging
from urllib2 import Request, urlopen, URLError
import json
from subprocess import Popen


WORDS = ["PLAY", "MUSIC"]

PRIORITY = 1


def handle(text, mic, profile):
    mic.say("OK.Playing music!")
    cmd = 'omxplayer -o local /home/pi/Music/ian1/1.mp3 &'
    proc =os.system(cmd)
    return

def isValid(text):
    wicky= bool(re.search(r'\bplay\b',text, re.IGNORECASE))
    article= bool(re.search(r'\bmusic\b',text, re.IGNORECASE))

    if wicky or article:
        return True
    else:
        return False