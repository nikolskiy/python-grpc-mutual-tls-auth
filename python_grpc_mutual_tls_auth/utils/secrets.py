from pathlib import Path


def load(path):
    with open(Path(path).expanduser(), 'rb') as f:
        data = f.read()
    return data
