from cpu import CPU
from pcode import Pcode
from time import sleep
import threading
import matplotlib.pyplot as plt
from window import Window
from windows_config import CPU_DEFAULT_FREQ

class System():
    def __init__(self):
        self._is_locked = True
        self.cpu = CPU(self)
        self._sub_colors = ['lightblue', 'lightsalmon', 'lightgreen', 'lightcoral']
        self._monitors = {}
        self.num_of_monitors = 0
        self._windows_events = []
        self.window = Window(self._windows_events)
        self._windows_events_red_flag = False
        self._windows_events_thread = threading.Thread(target=self._windows_events_handler)
        self._windows_events_thread.start()

        self._pcode = Pcode(self)
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
                    if event == 'stop prime95':
                        self.stop_prime95()
                    # if event == 'exit':
                    #     self.exit()

        
        return

    def start_cores_monitor(self, monitor_function):
        self.num_of_monitors += 1
        monitor_red_flag = False
        monitor_results = [[] for _ in range(self.cpu.num_of_cores)]
        monitor_thread = threading.Thread(target=self._monitor, args=(self.num_of_monitors,))
        self._monitors[self.num_of_monitors] = [monitor_function, monitor_red_flag, monitor_results, monitor_thread]
        
        monitor_thread.start()
        return self.num_of_monitors

    def stop_cores_monitor(self, monitor_id):
        monitor_function, monitor_red_flag, monitor_results, monitor_thread = self._monitors[monitor_id]

        self._monitors[monitor_id][1] = True
        monitor_thread.join()
        return monitor_results

    def _monitor(self, monitor_id):
        monitor_function, monitor_red_flag, monitor_results, _ = self._monitors[monitor_id]
        self.cores_freq_results = [[] for _ in range(self.cpu.num_of_cores)]

        while(not self._monitors[monitor_id][1]):
            for i, core in enumerate(self.cpu.get_cores_list()):
                self._monitors[monitor_id][2][i].append(monitor_function(core))
            sleep(0.5)

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
            print('stop_prime95 v')
            self.cpu._run_stress(-0.98)
        else:
            print('system is locked!')
        return

    def _show_single_plot(self, data_list, down_limit=0, up_limit=4400):
        for i in range(len(data_list)):
            ys = data_list[i]
            xs = range(len(ys))
            plt.plot(xs, ys)
            plt.ylim(down_limit, up_limit)
            plt.fill_between(xs, ys, color=self._sub_colors[i%4], alpha=0.3)

        plt.show()
        return

    def _show_multi_plot(self, data_list, down_limit=0, up_limit=4400):
        num_of_plots = len(data_list)
        if num_of_plots == 4:
            fig, axs = plt.subplots(2, 2)
            for i in range(num_of_plots):
                ys = data_list[i]
                xs = range(len(ys))
                axs[i%2][int(i/2)].plot(xs, ys)
                axs[i%2][int(i/2)].set_ylim(down_limit, up_limit)
                axs[i%2][int(i/2)].fill_between(xs, ys, color='lightblue', alpha=0.3)

        else:
            fig, axs = plt.subplots(1, num_of_plots)
            for i in range(num_of_plots):
                ys = data_list[i]
                xs = range(len(ys))
                axs[i].plot(xs, ys)
                axs[i].set_ylim(down_limit, up_limit)
                axs[i].fill_between(xs, ys, color='lightblue', alpha=0.3)

        plt.show()
        return

    def show_plot(self, data_list, single_plot=False, down_limit=0, up_limit=4400):
        if single_plot:
            self._show_single_plot(data_list, down_limit, up_limit)
        else:
            self._show_multi_plot(data_list, down_limit, up_limit)
        return

    def exit(self):
        self.cpu._exit()
        self._pcode._exit()
        self.window._exit()
        self._windows_events_red_flag = True
        self._windows_events_thread.join()
        self.window._running = False
        return

    def trigger(self, event):
        if event == '2Hot':
            print('2HOT')
            self.cpu.set_frequency_limit(800)
            self.window.syscode.set_code('2Hot')
        elif event == '2Hot_End':
            self.cpu.set_frequency_limit(CPU_DEFAULT_FREQ)
            self.window.syscode.set_code('0000')

