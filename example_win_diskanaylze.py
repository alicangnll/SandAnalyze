import sys, os
from classes.Windows_X86_64 import QilingSandBox_Windows_x86_64
print("======================================")
print("         SandAnalyze - Malware Analysis Tool           ")
print("Example : python3 example_win_diskanaylze.py example.bin nodebug / qdb / gdb")
print("======================================")
try:
    exeloc = str(sys.argv[1]) # .bin file
    try:
        debugger = str(sys.argv[2])
    except:
        debugger = "nodebug"
    QilingSandBox_Windows_x86_64.windisk_analyze(exeloc, debugger, 0)
except Exception as e:
    print("ERROR:" + str(e))