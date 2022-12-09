import capstone, pefile, sys
from unicorn.arm_const import *
from qiling import *
from qiling.const import *
from qiling.os import *
from capstone import *

class QilingSandBox_Windows:
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

    def my_sandbox(path, rootfs):
        ql = Qiling(path, rootfs)
        ql.debugger = "qdb"
        ql.run()

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
            QilingSandBox_Windows.my_sandbox([r"examples/rootfs/x8664_windows/bin/" + exeloc], r"examples/rootfs/x8664_windows")
        else:
            QilingSandBox_Windows.my_sandbox([r"examples/rootfs/x86_windows/bin/" + exeloc], r"examples/rootfs/x86_windows")