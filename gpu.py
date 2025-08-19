from core import Core

class GPU():
    def __init__(self, system, n=100):
        self._system = system
        self.num_of_PUs = n
        self._PUs_list = [Core(self._system) for _ in range(self.num_of_PUs)]
        self._wl = 0.1
        return

    def _exit(self):
        for pu in self._PUs_list:
            pu._exit()

    def _run_stress(self, n):
        self._wl += n
        frequency = self._culc_freq()
        for pu in self._PUs_list:
            pu._request_frequency(frequency)

    def _culc_freq(self):
        frequency = max(100, 100 + 0.2*pow(self._wl*100, 3))
        return min(frequency, 800)

    def get_PUs_list(self):
        return self._PUs_list

    def set_frequency_limit(self, limit):
        for pu in self._PUs_list:
            pu._frequency_limit = limit
