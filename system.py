from cpu import CPU
from time import sleep

class System():
    def __init__(self):
        self._is_locked = True
        self.cpu = CPU()
        return

    def unlock(self):
        self._is_locked = False

    def is_locked(self):
        return self._is_locked

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
        return

    # def start_prime95(self):
    #     if not self._is_locked:
            

    #     else:
    #         print('system is locked!')
