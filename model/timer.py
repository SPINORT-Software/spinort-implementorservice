import time
from typing import Callable

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""
    pass


class Timer:
    def __init__(self, minutes: int = 1, callback: Callable = None):
        self.minutes = minutes
        self.callback = callback

    def start(self):
        seconds = self.minutes * 60
        print(f"Timer set for {self.minutes} minute(s).")
        time.sleep(seconds)

    def execute_callback(self, **kwargs):
        if self.callback:
            self.callback(**kwargs)
