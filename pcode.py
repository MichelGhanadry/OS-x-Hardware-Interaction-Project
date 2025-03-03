from pcode_config import *
from time import time, sleep
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

    def _cpu_mode_check(self):
        while not self._red_flag:
            current_cpu_mode = self._get_cpu_mode()
            if current_cpu_mode == self._cpu_mode:
                self._cpu_mode_counter += 1
                if time() - self._cpu_mode_start_time > CPU_IDLE_TIME:
                    self._system.window._set_sleep_mode(mode=True)
                    self._cpu_mode = "sleep"
                    print("go to sleep")
            else:
                self._cpu_mode = current_cpu_mode
                self._cpu_mode_counter = 0
                self._cpu_mode_start_time = time()
            sleep(0.1)

        return

    def _get_cpu_mode(self):
        for core in self._cores:
            if core.get_frequency() > CPU_IDLE_FREQ:
                return "stress"
        return "idle"

    def wake_system(self):
        self._system.window._set_sleep_mode(mode=False)

