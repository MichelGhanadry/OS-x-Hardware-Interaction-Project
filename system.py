from cpu import CPU
from time import sleep
import threading
from window import Window

class System():
    def __init__(self):
        self._is_locked = True
        self.cpu = CPU()

        self._windows_events = []
        self.window = Window(self._windows_events)
        self._windows_events_red_flag = False
        self._windows_events_thread = threading.Thread(target=self._windows_events_handler)
        self._windows_events_thread.start()
        return

    def unlock(self):
        self._is_locked = False

    def is_locked(self):
        return self._is_locked

    def _windows_events_handler(self):
        while not self._windows_events_red_flag:
            if len(self._windows_events) > 0:
                for event in self._windows_events:
                    self._windows_events.remove(event)
                    if event == 'start prime95':
                        self.start_prime95()
                    # if event == 'exit':
                    #     self.exit()

        
        return

    def wait(self, n):
        print(f'waiting for {n} sec')
        sleep(n)

    def start_prime95(self):
        if not self._is_locked:
            self.cpu._run_stress(0.98)
        else:
            print('system is locked!')
        return

    def stop_prime95(self):
        if not self._is_locked:
            self.cpu._run_stress(-0.98)
        else:
            print('system is locked!')
        return

    def exit(self):
        self.cpu._exit()
        self._windows_events_red_flag = True
        self._windows_events_thread.join()
        self.window._running = False
        return
