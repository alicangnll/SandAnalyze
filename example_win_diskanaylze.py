import sys, os
from classes.Windows_X86_64 import QilingSandBox_Windows_x86_64

try:
    binfile = sys.argv[1] # .bin file
    QilingSandBox_Windows_x86_64.windisk_analyze([os.getcwd() + "/examples/rootfs/x8664_windows/bin/" + binfile], 0)
except Exception as e:
    print("ERROR:" + str(e))