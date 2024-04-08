import sys, os
from classes.iOS import *

filelist = os.listdir("exefiles")
try:
    exeloc = str(sys.argv[1])
    type = str(sys.argv[2])
    debugger = str(sys.argv[3])
except IndexError:
    print("Example : python3 example.py example_ios_arm64 arm64 / arm  nodebug / gdb / qdb")
except:
    print("""
          [*] Since no architect (arm / arm64) is selected, it is selected 'arm'
          OR
          [*] Since no debugger (gdb / qdb) is selected, will not debugging!
          """)
    debugger = "nodebug"
    type = "arm"
    
if exeloc is None or exeloc == "" or type is None or type == "" or debugger is None or debugger == "":
    print("Example : python3 example.py example_ios_arm64 arm64 / arm  nodebug / gdb / qdb")
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