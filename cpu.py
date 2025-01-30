from core import Core

class CPU():
    def __init__(self, n=4):
        self.num_of_cores = n
        self._cores_list = [Core() for _ in range(self.num_of_cores)]
        self._wl = 0.1

        self.WF = {

        }
        return

    def _exit(self):
        for core in self._cores_list:
            core._exit()

    def _run_stress(self, n):
        self._wl += n
        frequency = self._culc_freq()
        for core in self._cores_list:
            core._request_frequency(frequency)

    def _culc_freq(self):
        frequency = max(400, 400 + 0.35*pow(self._wl*100, 2))
        return min(frequency, 4000)

    def get_cores_list(self):
        return self._cores_list
