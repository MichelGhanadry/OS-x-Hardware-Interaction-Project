from core import Core

class CPU():
    def __init__(self, n=4):
        self.num_of_cores = n
        self._cores_list = [Core() for _ in range(self.num_of_cores)]
        return

    def _exit(self):
        for core in self._cores_list:
            core._exit()

    def get_cores_list(self):
        return self._cores_list
