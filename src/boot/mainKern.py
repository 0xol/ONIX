import boot.kernel.mem as mem

def kern_main():
    print("[KERNEL] Starting ONIX v0.1")
    print(f"[KERNEL] Total memory detected: {mem.getTotalMem() / 1024}kb")