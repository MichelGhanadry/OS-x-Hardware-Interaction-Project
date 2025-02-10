from system import System

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

cores = system.cpu.get_cores_list()

system.start_cores_freqency_monitor()
system.wait(5)
data = system.stop_cores_freqency_monitor()
system.show_plot(data, single_plot=False)

########################################################################

system.exit()