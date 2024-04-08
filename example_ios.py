import sys, os
from classes.iOS import *

filelist = os.listdir("exefiles")
try:
    exeloc = str(sys.argv[1])
    debugger = str(sys.argv[2])
except IndexError:
    print("Example : python3 example_ios.py example_ios_arm64 nodebug / gdb / qdb")
except:
    print("""
          [*] Since no architect (arm / arm64) is selected, it is selected 'arm'
          OR
          [*] Since no debugger (gdb / qdb) is selected, will not debugging!
          """)
    debugger = "nodebug"
    
if exeloc is None or exeloc == "" or debugger is None or debugger == "":
    print("Example : python3 example_ios.py example_ios_arm64  nodebug / gdb / qdb")
else:
    if debugger == "qdb" or debugger == "gdb":
            try:
                TestiOS.debug_ios_arm64(exeloc, debugger)
            except Exception as e:
                   print("ERROR: " + str(e))
    else:
        try:
            TestiOS.test_ios_arm64(exeloc)
        except Exception as e:
             print("ERROR: " + str(e))