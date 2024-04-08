import sys
from classes.Windows_X86_64 import *
from classes.Linux_X86_64 import *

print("======================================")
print("         SandAnalyze - Malware Analysis Tool           ")
print("Example : python3 example.py example.exe nodebug / gdb / qdb")
print("======================================")

try:
    exeloc = str(sys.argv[1])
    debugger = str(sys.argv[2])
except IndexError:
    print("Example : python3 example.py example.exe nodebug / gdb / qdb")
except:
    print("""
          [*] Since no debugger (gdb / qdb) is selected, it is debugged with 'qdb'
          """)
    debugger = "qdb"
    
if exeloc is None or exeloc == "" or debugger is None or debugger == "":
    print("Example : python3 example.py example.exe nodebug / gdb / qdb")
else:
    QilingSandBox_Windows_x86_64.sandbox_analyze(exeloc, debugger)