import os

def colorize(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }
def decorator(func):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return f"{colors.get(color, '')}{text}{colors['reset']}"
        return wrapper
    return decorator

class FileReader:
    def __init__(self, filepath: str):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"{filepath} does not exist.")
        self._filepath = filepath

 @property
    def filepath(self) -> str:
        return self._filepath
