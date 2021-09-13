# copy module
class cpu:
    pass

class disk:
    pass

class computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = cpu()
cpu2 = cpu1
print(id(cpu1), id(cpu2), sep='\n')

import copy
disk1 = disk()
computer1 = computer(cpu1, disk1)
print(disk1)
computer2 = copy.copy(computer1)
print(computer1, computer1.cpu, computer1.disk, sep='\n')
print(computer2, computer2.cpu, computer2.disk, sep='\n')

