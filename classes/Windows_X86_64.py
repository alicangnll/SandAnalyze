import capstone, pefile, sys, random, os
from qiling import *
from qiling.const import *
from qiling.os import *
from capstone import *
from qiling.const import QL_VERBOSE
from qiling.os.mapper import QlFsMappedObject


class Fake_Drive(QlFsMappedObject):
    def read(self, size):
        return random.randint(0, 256)
    def write(self, bs):
        return len(bs)      
    def fstat(self):
        return -1
    def close(self):
        return 0

class QilingSandBox_Windows_x86_64:
    def pe_load(pe):
        entry_point = pe.OPTIONAL_HEADER.AddressOfEntryPoint
        data = pe.get_memory_mapped_image()[entry_point:]
        return capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32).disasm(data, 0x10000)
    
    def arch(pe):
        if pe.FILE_HEADER.Machine == 0x14c:
            bit = 32
        elif pe.FILE_HEADER.Machine == 0x8664:
            bit = 64
        return bit

    def GetProcAddress(ql, addr, params):
        print(params)
        return addr, params

    def stop(ql):
        ql.nprint("[+] Address found")
        ql.emu_stop()

    def my_sandbox(path, rootfs = os.getcwd() + "/examples/rootfs/x8664_windows", debugger = "gdb"):
        ql = Qiling(path, r"" + rootfs, verbose=QL_VERBOSE.DEBUG)
        ql.debugger = str(debugger)
        ql.run(timeout=5000)

    def shellcode_sandbox(path, rtfs, shellcode, debugger = "gdb"):
        ql = Qiling(shellcoder=shellcode, rootfs=r"" + rtfs, verbose=QL_VERBOSE.DEBUG)
        ql.debugger = str(debugger)
        ql.run(timeout=5000)

    def stopatkillerswtich(ql: Qiling):
        print("WannaCry Detected!")
        QilingSandBox_Windows_x86_64.stop(ql)
        return True

    def wannacry_hunter(path, rootfs = os.getcwd() + "/examples/rootfs/x8664_windows", memloc = 0x40819a):
        ql = Qiling(r"" + path, r"" + rootfs, verbose=QL_VERBOSE.DEBUG)
        found = ql.hook_address(QilingSandBox_Windows_x86_64.stopatkillerswtich, memloc)
        if found is True:
            return True
        else:
            return False
    
    # Anaylzer for Windows
    def windisk_analyze(path, rootfs, driveid, debugger = "gdb"):
        ql = Qiling(r"" + path, r"" + rootfs, verbose=QL_VERBOSE.DEBUG)
        ql.add_fs_mapper(r"\\.\PHYSICALDRIVE" + int(driveid) + "", Fake_Drive())
        ql.debugger = str(debugger)
        ql.run(timeout=5000)

    def sandbox_analyze(exeloc, debugger):
        try:
            QilingSandBox_Windows_x86_64.pe_load(pefile.PE("examples/rootfs/x8664_windows/bin/" + exeloc))
        except OSError as e:
            print(e)
            sys.exit()
        except pefile.PEFormatError as e:
            print("[-] PEFormatError: %s" % e.value)
            print("[!] The file is not a valid PE")
            sys.exit()
        arch = str(QilingSandBox_Windows_x86_64.arch(pefile.PE(os.getcwd() + "/examples/rootfs/x8664_windows/bin/" + exeloc)))
        print("[+] Arch : " + arch)
        if(arch == "64"):
            QilingSandBox_Windows_x86_64.my_sandbox([os.getcwd() + "/examples/rootfs/x8664_windows/bin/" + exeloc],  os.getcwd() + "/examples/rootfs/x8664_windows", debugger)
        else:
            QilingSandBox_Windows_x86_64.my_sandbox([os.getcwd() + "/examples/rootfs/x86_windows/bin/" + exeloc], os.getcwd() + "/examples/rootfs/x8664_windows", debugger)
