from system import System
from core import Core

system = System()
system.unlock()

########################################################################

# for i, core in enumerate(system.cpu.get_cores_list()):
#     print(f"core{i} freq is {core.get_frequency()}MHz")

# system.start_prime95()
# system.wait(5)

# for i, core in enumerate(system.cpu.get_cores_list()):
#     print(f"core{i} freq is {core.get_frequency()}MHz")

########################################################################

# cores = system.cpu.get_cores_list()

# system.start_cores_freqency_monitor()
# system.wait(5)
# data = system.stop_cores_freqency_monitor()
# system.show_plot(data, single_plot=False)

########################################################################

# cores = system.cpu.get_cores_list()

# frequency_monitor = system.start_cores_monitor(Core.get_frequency)
# tempreture_monitor = system.start_cores_monitor(Core.get_tempreture)
# system.wait(5)
# system.start_prime95()
# system.wait(20)
# tempreture_data = system.stop_cores_monitor(tempreture_monitor)
# frequency_data = system.stop_cores_monitor(frequency_monitor)

# system.show_plot(frequency_data, single_plot=False, down_limit=20, up_limit=4400)
# system.show_plot(tempreture_data, single_plot=False, down_limit=20, up_limit=44)

########################################################################

system.wait(60)
# system._pcode.create_timeline()

########################################################################

# frequency_monitor = system.start_cores_monitor(Core.get_frequency)
# gpu_monitor = system.start_gpu_monitor(Core.get_frequency)
# system.wait(10)
# system.start_prime95()
# system.wait(15)
# system.stop_prime95()
# system.wait(20)
# system.start_video()
# system.wait(15)
# system.stop_video()
# system.wait(10)
# gpu_data = system.stop_gpu_monitor(gpu_monitor)
# frequency_data = system.stop_cores_monitor(frequency_monitor)

# system.show_plot(frequency_data, single_plot=True, down_limit=20, up_limit=4400)
# system.show_gpu_plot(gpu_data, down_limit=20, up_limit=1000)

########################################################################

# gpu_monitor = system.start_gpu_monitor(Core.get_frequency)
# system.wait(3)
# system.start_video()
# system.wait(8)
# gpu_data = system.stop_gpu_monitor(gpu_monitor)

# system.show_multi_gpu_plot(gpu_data, down_limit=20, up_limit=1000)

########################################################################

# frequency_monitor = system.start_cores_monitor(Core.get_frequency)
# tempreture_monitor = system.start_cores_monitor(Core.get_tempreture)
# system.wait(1)
# system.start_prime95()
# system.wait(
# tempreture_data = system.stop_cores_monitor(tempreture_monitor)
# frequency_data = system.stop_cores_monitor(frequency_monitor)

# system.show_plot(frequency_data, single_plot=True, down_limit=20, up_limit=4400)
# system.show_plot(tempreture_data, single_plot=True, down_limit=20, up_limit=44)

system.exit()


# frequency = max(400, 400 + 0.35*pow(self._wl*100, 2))
