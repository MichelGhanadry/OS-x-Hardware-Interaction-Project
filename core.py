import random
import threading
from time import sleep

MIN_FREQ = 400
MAX_FREQ = 4000

class Core():
    def __init__(self):
        self.frequency = 400
        self._state = 'idle'
        self._frequency_limit = MAX_FREQ
        return

    def _set_frequency(self, freq):
        self.frequency = freq
        return

    def get_frequency(self):
        return self.frequency

