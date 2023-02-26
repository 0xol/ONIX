import sys
sys.path.append("/boot")
sys.path.append("/boot/kernel")

import boot.mainKern

boot.mainKern.kern_main()
while True:
    pass