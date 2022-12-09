import capstone, pefile, sys, time, socket
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
        ql.console = False
        ql.emu_stop()

    def my_sandbox(path, rootfs):
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DEBUG)
        ql.os.set_api("GetProcAddress", QilingSandBox_Windows.GetProcAddress, QL_INTERCEPT.EXIT)
        ql.hook_address(QilingSandBox_Windows.stop, 0x0042B726)
        #WannaCry : ql.hook_address(stopatkillerswtich, 0x40819a)
        ql.filter = ("open")
        ql.debugger = "qdb"
        ql.run()

    def runwindows(exeloc):
        try:
            QilingSandBox_Windows.pe_load(pefile.PE("examples/rootfs/x8664_windows/Windows/bin/" + exeloc))
        except:
            print("Somethings went wrong!")
            sys.exit()

        print("[+] Arch : " + str(QilingSandBox_Windows.arch(pefile.PE("examples/rootfs/x8664_windows/Windows/bin/" + exeloc))))
        QilingSandBox_Windows.my_sandbox([r"examples/rootfs/x8664_windows/Windows/bin/" + exeloc], r"examples/rootfs/x8664_windows")

class SimpleGdbClient:
    DELAY = 0.6
    def __init__(self, host: str, port: int):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        txtf = sock.makefile('w')

        sock.connect((host, port))

        self.__sock = sock
        self.__file = txtf

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.__sock.close()

    @staticmethod
    def checksum(data: str) -> int:
        return sum(ord(c) for c in data) & 0xff

    def send(self, msg: str):
        time.sleep(SimpleGdbClient.DELAY)

        self.__file.write(f'${msg}#{SimpleGdbClient.checksum(msg):02x}')
        self.__file.flush()
