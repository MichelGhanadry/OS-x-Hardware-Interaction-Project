import random
import threading
from time import sleep

ERROR_BAR = 50
MIN_FREQ = 400
MAX_FREQ = 4000

class Core():
    def __init__(self):
        self.red_flag = False
        self.frequency = 400
        self._target_frequency = 400
        self._state = 'idle'
        self._up_tau = 5
        self._down_tau = 12

        self._step = 0
        self._steps_count = 0

        self._thread = threading.Thread(target=self._update_frequency)
        self._thread.start()
        return

    def _set_frequency(self, freq):
        self.frequency = freq
        return

    def _request_frequency(self, target_frequency):
        freq_delta = target_frequency - self.frequency
        tau = self._up_tau if freq_delta > 0 else self._down_tau
        
        self._step = int(freq_delta / tau)
        self._steps_count = tau
        self._target_frequency = target_frequency
        return

    def _update_frequency(self):
        while(not self.red_flag):
            delta = random.randint(0, 2*ERROR_BAR) - ERROR_BAR
            frequency = int(self.frequency + delta)
            frequency = max(MIN_FREQ, frequency)
            frequency = min(MAX_FREQ, frequency)

            if self._steps_count > 0:
                print(f'self.frequency={self.frequency} self._step={self._step} self._steps_count={self._steps_count}')
                self.frequency += self._step
                self._steps_count -= 1
            else:
                self.frequency = self._target_frequency

            delta = random.randint(0, 2*ERROR_BAR) - ERROR_BAR
            frequency = int(self.frequency + delta)
            frequency = max(MIN_FREQ, frequency)
            frequency = min(MAX_FREQ, frequency)
            self.frequency = frequency
            if self.frequency > MAX_FREQ or self.frequency < MIN_FREQ:
                print('freq error')

            sleep(0.01)

    def get_frequency(self):
        sleep(0.001)
        return self.frequency
    
    def _exit(self):
        self.red_flag = True
        self._thread.join()
        return