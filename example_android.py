import sys, os
from classes.Android import *

filelist = os.listdir("exefiles")
try:
    exeloc = str(sys.argv[1])
    type = str(sys.argv[2])
    debugger = str(sys.argv[3])
except IndexError:
    print("Example : python3 example.py example_android_arm arm64 / arm  nodebug / gdb / qdb")
except:
    print("""
          [*] Since no architect (arm / arm64) is selected, it is selected 'arm'
          OR
          [*] Since no debugger (gdb / qdb) is selected, will not debugging!
          """)
    debugger = "nodebug"
    type = "arm"
    
if exeloc is None or exeloc == "" or type is None or type == "" or debugger is None or debugger == "":
    print("Example : python3 example.py example_android_arm arm64 / arm  nodebug / gdb / qdb")
else:
    if type == "arm64":
        if debugger == "qdb" or debugger == "gdb":
            try:
                TestAndroid.debug_android_arm64(exeloc, debugger)
            except Exception as e:
                print("ERROR: " + str(e))
        else:
            try:
                TestAndroid.test_android_arm64(exeloc)
            except Exception as e:
                print("ERROR: " + str(e))
    else:
        if debugger == "qdb" or debugger == "gdb":
            try:
                TestAndroid.debug_android_arm(exeloc, debugger)
            except Exception as e:
                print("ERROR: " + str(e))
        else:
            try:
                TestAndroid.test_android_arm64(exeloc)
            except Exception as e:
                print("ERROR: " + str(e))