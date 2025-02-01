from system import System

system = System()
system.unlock()

for i, core in enumerate(system.cpu.get_cores_list()):
    print(f"core{i} freq is {core.get_frequency()}MHz")

system.start_prime95()
system.wait(5)

for i, core in enumerate(system.cpu.get_cores_list()):
    print(f"core{i} freq is {core.get_frequency()}MHz")
