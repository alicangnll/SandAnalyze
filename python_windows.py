import capstone, pefile, sys, random
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
<<<<<<< Updated upstream
        print(bs)
=======
>>>>>>> Stashed changes
        return len(bs)      
    def fstat(self):
        return -1
    def close(self):
        return 0

class QilingSandBox_Windows:
    def pe_load(pe):
        entry_point = pe.OPTIONAL_HEADER.AddressOfEntryPoint
        data = pe.get_memory_mapped_image()[entry_point:]
        return capstone.Cs(capstone.CS_ARCH_X86, capstone.CS_MODE_32).disasm(data, 0x10000)
<<<<<<< Updated upstream

    def hook(ql, force_call_dialog_func, basecode):
        ql.hook_address(force_call_dialog_func, basecode)
=======
>>>>>>> Stashed changes
    
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

    def my_sandbox(path, rootfs, arch):
        ql = Qiling(path, rootfs, archtype=arch, ostype="windows", verbose=QL_VERBOSE.DEBUG)
<<<<<<< Updated upstream
        ql.debugger = "qdb"
        ql.run(timeout=5000)

    def windisk_analyze(path, rootfs):
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DEBUG)
        ql.add_fs_mapper(r"\\.\PHYSICALDRIVE0", Fake_Drive.read())
        ql.run()
=======
        ql.debugger = "qdb"
        ql.run(timeout=5000)

    def shellcode_sandbox(path, rtfs, arch, shellcode):
        ql = Qiling(shellcoder=shellcode, rootfs=rtfs, ostype="windows", archtype=arch)
        ql.debugger = "qdb"
        ql.run(timeout=5000)
        
    def windisk_analyze(path, rootfs, driveid):
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DEBUG)
        ql.add_fs_mapper(r"\\.\PHYSICALDRIVE" + driveid + "", Fake_Drive())
        ql.debugger = "qdb"
        ql.run(timeout=5000)
>>>>>>> Stashed changes

    def runwindows(exeloc):
        try:
            QilingSandBox_Windows.pe_load(pefile.PE("examples/rootfs/x8664_windows/bin/" + exeloc))
        except OSError as e:
            print(e)
            sys.exit()
        except pefile.PEFormatError as e:
            print("[-] PEFormatError: %s" % e.value)
            print("[!] The file is not a valid PE")
            sys.exit()
        arch = str(QilingSandBox_Windows.arch(pefile.PE("examples/rootfs/x8664_windows/bin/" + exeloc)))
        print("[+] Arch : " + str(QilingSandBox_Windows.arch(pefile.PE("examples/rootfs/x8664_windows/bin/" + exeloc))))
        if(arch == "64"):
            QilingSandBox_Windows.my_sandbox([r"examples/rootfs/x8664_windows/bin/" + exeloc], r"examples/rootfs/x8664_windows", arch)
        else:
<<<<<<< Updated upstream
            QilingSandBox_Windows.my_sandbox([r"examples/rootfs/x86_windows/bin/" + exeloc], r"examples/rootfs/x86_windows", arch)
=======
            QilingSandBox_Windows.my_sandbox([r"examples/rootfs/x86_windows/bin/" + exeloc], r"examples/rootfs/x86_windows", arch)
>>>>>>> Stashed changes
