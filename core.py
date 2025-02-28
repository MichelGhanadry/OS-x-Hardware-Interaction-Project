import random
import threading
from time import sleep
from windows_config import *

ERROR_BAR = 50
MIN_FREQ = 400
MAX_FREQ = 4000

class Core():
    def __init__(self, system):
        self._system = system
        self.red_flag = False
        self.frequency = 400
        self.tempreture = 24
        self._target_frequency = 400
        self._state = 'idle'
        self._up_tau = 5
        self._down_tau = 12
        self._frequency_limit = CPU_DEFAULT_FREQ
        self._requested_frequency_limit = CPU_DEFAULT_FREQ

        self._step = 0
        self._steps_count = 0
        self._tempreture_tau = 1
        self._thermal_2hot_counter = 0

        self._update_frequency_thread = threading.Thread(target=self._update_frequency)
        self._update_frequency_thread.start()

        self._update_tempreture_thread = threading.Thread(target=self._update_tempreture)
        self._update_tempreture_thread.start()
        return

    def _set_frequency(self, freq):
        self.frequency = freq
        return

    def _exit(self):
        self.red_flag = True
        self._update_frequency_thread.join()
        self._update_tempreture_thread.join()
        return

    def _request_frequency(self, target_frequency):
        self._target_frequency = target_frequency
        freq_delta = self._target_frequency - self.frequency
        tau = self._up_tau if freq_delta > 0 else self._down_tau
        
        self._step = int(freq_delta / tau)
        self._steps_count = tau
        print(f'self._steps_count {self._steps_count}')
        print(f'self._step {self._step}')
        return

    def _set_frequency_limit(self, limit):
        self._request_frequency(limit)
        self._requested_frequency_limit = limit
        return

    def _update_frequency(self):
        while(not self.red_flag):
            delta = random.randint(0, 2*ERROR_BAR) - ERROR_BAR
            frequency = int(self.frequency + delta)
            # frequency = max(MIN_FREQ, frequency)
            # frequency = min(MAX_FREQ, frequency)

            if self._steps_count > 0:
                print(f'self.frequency={self.frequency} self._step={self._step} self._steps_count={self._steps_count}')
                self.frequency += self._step
                self._steps_count -= 1
            else:
                print(f'self.frequency={self.frequency} self._step={self._step} self._steps_count={self._steps_count}')
                self.frequency = self._target_frequency

            delta = random.randint(0, 2*ERROR_BAR) - ERROR_BAR
            frequency = int(self.frequency + delta)
            frequency = max(MIN_FREQ, frequency)
            frequency = min(self._frequency_limit, frequency)
            frequency = min(MAX_FREQ, frequency)
            self.frequency = frequency
            if self.frequency > MAX_FREQ or self.frequency < MIN_FREQ:
                print('freq error')

            sleep(0.3)
        return

    def _update_tempreture(self):
        down_flag = False
        while(not self.red_flag):
            if self.frequency >= 3000:
                target_tempreture = self.tempreture + 1
            if self.frequency > 1000 and self.frequency < 3000:
                target_tempreture = self.tempreture + random.randint(0, 2) - 1
            if self.frequency <= 1000:
                if down_flag:
                    target_tempreture = self.tempreture - 3
                else:
                    target_tempreture = self.tempreture
                down_flag = not down_flag

            self.tempreture = max(24, target_tempreture)
            sleep(self._tempreture_tau)
            if self.tempreture > 40 and self._thermal_2hot_counter == 0:
                self._thermal_2hot_counter = CYCLES_2HOT
                self._system.trigger(event='2Hot') # start new 2Hot event

            if self.tempreture < 40 and self._thermal_2hot_counter > 0:
                # we have 2Hot event and we started to cool down
                self._thermal_2hot_counter -= 1
                if self._thermal_2hot_counter == 0:
                    self._system.trigger(event='2Hot_End')

        return

    def get_frequency(self):
        sleep(0.001)
        return self.frequency

    def get_tempreture(self):
        sleep(0.001)
        return self.tempreture

