import sys, os
from python_windows import *
from python_linux import *
print("""
      # Run dllscollector.bat
      Create a folder inside of examples/rootfs/windows_xx/bin
      Copy malware inside of examples/rootfs/windows_xx/bin
      Example EXE name : example.exe
      """)

filelist_x86 = os.listdir(os.getcwd() + "/examples/rootfs/x86_windows/bin")
filelist_x8664 = os.listdir(os.getcwd() + "/examples/rootfs/x8664_windows/bin")
print("=========================================")
print("x86 File List")
print("=========================================")
for i in filelist_x86:
    print("[*] " + i + "\n")
print("=========================================")
print("x64 File List")
print("=========================================")
for i in filelist_x8664:
    print("[*] " + i + "\n")
exeloc = str(sys.argv[1])
if exeloc is None or exeloc == "":
    print("Example example.py example.exe")
else:
    try:
        QilingSandBox_Windows.runwindows(exeloc)
    except:
        print("Example example.py example.exe")