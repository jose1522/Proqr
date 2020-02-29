from pathlib import Path
import os


def readDBKey():
    path = Path(os.getcwd())
    path = os.path.join(path, 'app','objects', 'keys', 'db')
    with open(path) as t:
        key = t.read()
    return key

def readSendGridKey():
    path = Path(os.getcwd())
    path = os.path.join(path, 'app','objects', 'keys', 'sendgrid')
    with open(path) as t:
        key = t.read()
    return key