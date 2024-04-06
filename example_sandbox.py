import sys, os
from classes.Windows_X86_64 import *
from classes.Linux_X86_64 import *

filelist = os.listdir("exefiles")
try:
    exeloc = str(sys.argv[1])
    try:
        debugger = str(sys.argv[2])
    except:
        print("""
            [*] Since no debugger (gdb / qdb) is selected, it is debugged with 'qdb'
              """)
        debugger = "qdb"
    if exeloc is None or exeloc == "":
        print("Example example.py example.exe")
    else:
        try:
            QilingSandBox_Windows_x86_64.sandbox_analyze(exeloc, debugger)
        except:
            print("""
                  =========================================
                  File List
                  =========================================
                  """)
            for i in filelist:
                print("[*] " + i + "\n")
            print("Example example.py example.exe")
except IndexError:
    print("""
          =========================================
          File List
          =========================================
          """)
    for i in filelist:
        print("[*] " + i + "\n")
    print("""
      # Run dllscollector.bat
      Create a folder inside of examples/rootfs/windows_xx/bin
      Copy malware inside of examples/rootfs/windows_xx/bin
      Example command : python3 example.py example.exe 
      """)
except Exception as e:
    print("ERROR : " + str(e))