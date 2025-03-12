from pcode_config import *
from time import time, sleep
import threading
from timeline import show_timeline

class Pcode():
    def __init__(self, system):
        self._system = system
        self._cores = self._system.cpu.get_cores_list()

        self._cpu_mode = "idle"
        self._cpu_mode_counter = 0
        self._absolute_start_time = time()
        self._cpu_mode_start_time = self._absolute_start_time
        self.states_timeline_list = [(self._cpu_mode, self._cpu_mode_start_time)]

        self._cpu_mode_thread_flag = False
        self._cpu_mode_thread = threading.Thread(target=self._cpu_mode_check)
        self._cpu_mode_thread.start()
        return

    def _exit(self):
        self._cpu_mode_thread_flag = True
        self._cpu_mode_thread.join()
        return

    def _cpu_mode_check(self):
        while not self._cpu_mode_thread_flag:
            current_cpu_mode = self._get_cpu_mode()
            if current_cpu_mode == self._cpu_mode:
                self._cpu_mode_counter += 1

                if self._cpu_mode == "idle":
                    if time() - self._cpu_mode_start_time > CPU_IDLE_TIME:
                        self._system.window._set_sleep_mode(mode=True)
                        self._switch_cpu_mode(new_mode="sleep")
                        print("go to sleep")
            else:
                self._switch_cpu_mode(new_mode=current_cpu_mode)
                
            sleep(0.1)
            print(self._cpu_mode)
        return

    def _get_cpu_mode(self):
        if self._cpu_mode == "sleep":
            return self._cpu_mode
        
        for core in self._cores:
            if core.get_frequency() > CPU_IDLE_FREQ:
                return "stress"
        return "idle"

    def wake_system(self):
        self._system.window._set_sleep_mode(mode=False)
        self._switch_cpu_mode(new_mode="idle")
        return

    def _switch_cpu_mode(self, new_mode):
        self._cpu_mode = new_mode
        self._cpu_mode_counter = 0
        self._cpu_mode_start_time = time()
        self.states_timeline_list.append((self._cpu_mode, self._cpu_mode_start_time))
        return
    
    def create_timeline(self):
        d = self._absolute_start_time
        timelines = []
        clk_point = 0
        state = self.states_timeline_list[0]
        for next_state in self.states_timeline_list[1:] + [(self._cpu_mode , time())]:
            state_duration = next_state[1] - state[1]
            timelines.append((clk_point, clk_point+state_duration, state[0]))
            state = next_state
            clk_point += state_duration

        print(self.states_timeline_list)
        print(timelines)
        show_timeline(data=timelines, states=["sleep", "idle", "stress"])
        return

