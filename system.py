from cpu import CPU
from time import sleep
import threading
import matplotlib.pyplot as plt
from window import Window

class System():
    def __init__(self):
        self._is_locked = True
        self.cpu = CPU()
        self._sub_colors = ['lightblue', 'lightsalmon', 'lightgreen', 'lightcoral']

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

    def start_cores_freqency_monitor(self):
        self.cores_freq_red_flag = False
        self.cores_freq_results = [[] for _ in range(self.cpu.num_of_cores)]
        self.cores_freq_thread = threading.Thread(target=self._cores_freq_monitor)
        self.cores_freq_thread.start()

    def stop_cores_freqency_monitor(self):
        self.cores_freq_red_flag = True
        self.cores_freq_thread.join()
        return self.cores_freq_results

    def _cores_freq_monitor(self):
        self.cores_freq_results = [[] for _ in range(self.cpu.num_of_cores)]

        while(not self.cores_freq_red_flag):
            for i, core in enumerate(self.cpu.get_cores_list()):
                self.cores_freq_results[i].append(core.get_frequency())
            sleep(0.1)

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

    def _show_single_plot(self, data_list):
        for i in range(len(data_list)):
            ys = data_list[i]
            xs = range(len(ys))
            plt.plot(xs, ys)
            plt.ylim(0, 4400)
            plt.fill_between(xs, ys, color=self._sub_colors[i%4], alpha=0.3)

        plt.show()
        return

    def _show_multi_plot(self, data_list):
        num_of_plots = len(data_list)
        if num_of_plots == 4:
            fig, axs = plt.subplots(2, 2)
            for i in range(num_of_plots):
                ys = data_list[i]
                xs = range(len(ys))
                axs[i%2][int(i/2)].plot(xs, ys)
                axs[i%2][int(i/2)].set_ylim(0, 4400)
                axs[i%2][int(i/2)].fill_between(xs, ys, color='lightblue', alpha=0.3)

        else:
            fig, axs = plt.subplots(1, num_of_plots)
            for i in range(num_of_plots):
                ys = data_list[i]
                xs = range(len(ys))
                axs[i].plot(xs, ys)
                axs[i].set_ylim(0, 4400)
                axs[i].fill_between(xs, ys, color='lightblue', alpha=0.3)

        plt.show()
        return

    def show_plot(self, data_list, single_plot=False):
        if single_plot:
            self._show_single_plot(data_list)
        else:
            self._show_multi_plot(data_list)
        return

    def exit(self):
        self.cpu._exit()
        self._windows_events_red_flag = True
        self._windows_events_thread.join()
        self.window._running = False
        return


    # def start_prime95(self):
    #     if not self._is_locked:
            

    #     else:
    #         print('system is locked!')
