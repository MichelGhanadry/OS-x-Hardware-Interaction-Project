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

cores = system.cpu.get_cores_list()

frequency_monitor = system.start_cores_monitor(Core.get_frequency)
tempreture_monitor = system.start_cores_monitor(Core.get_tempreture)
system.wait(30)
tempreture_data = system.stop_cores_monitor(tempreture_monitor)
frequency_data = system.stop_cores_monitor(frequency_monitor)

system.show_plot(frequency_data, single_plot=False, down_limit=20, up_limit=4400)
system.show_plot(tempreture_data, single_plot=False, down_limit=20, up_limit=44)

########################################################################

system.exit()