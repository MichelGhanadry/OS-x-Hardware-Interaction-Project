from pcode_config import *
from time import time
import threading

class Pcode():
    def __init__(self, system):
        self._system = system
        self._cores = self._system.cpu.get_cores_list()

        self._cpu_mode = "idle"
        self._cpu_mode_counter = 0
        self._cpu_mode_start_time = time()

        self._red_flag = False
        self._cpu_mode_thread = threading.Thread(target=self._cpu_mode_check)
        self._cpu_mode_thread.start()
        return

    def _exit(self):
        self._red_flag = True
        self._cpu_mode_thread.join()
        return

    def _check_cpu_mode(self):
        for core in self._cores:
            if core.get_frequency() > CPU_IDLE_FREQ:
                return "stress"
        return "idle"

