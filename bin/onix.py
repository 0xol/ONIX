import component
import os

print("ONIX v1 STARTED")

for drive in component.find_components("drive"):
    print("[DRIVE] ", end="")
    print(drive.getLabel(), end=" ")
    print(drive.getCapacity(), end=" bytes\n")

for rom in component.find_components("eeprom"):
    print("[ROM]", end=" ")
    print(rom.getLabel(), end=" ")
    print(len(rom.get()), end="/")
    print(rom.getSize(), end=" bytes\n")

for filesystem in component.find_components("filesystem"):
    print("[FS] ", end="")
    print(filesystem.getLabel(), end=" ")
    print(filesystem.spaceUsed(), end="/")
    print(filesystem.spaceTotal(), end=" bytes\n")

computer = component.get("computer")
import gc

print("[MEM] ", end="")
print(str(gc.mem_alloc() / 1024).split(".")[0], end="/")
print(str((gc.mem_free() + gc.mem_alloc()) / 1024).split(".")[0], end=" kbytes used\n")

print("[VFS] Starting virtual file system... ", end="")
import fs
fs.init()
print("[INIT] Starting user processes... ", end="")
from shell import spawn
spawn("/bin/init.py")

while True:
    pass