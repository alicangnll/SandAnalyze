from qiling import Qiling
from qiling.const import QL_VERBOSE
from qiling.exception import *

class QilingSandbox_Linux_X86_64:
    def test_libpatch_elf_linux_x8664(path, rootfs):
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DEBUG)
        ql.patch(0x0000000000000575, b'qiling\x00', target='libpatch_test.so')
        ql.run()
        
    def test_elf_linux_x86(path, rootfs):
        ql = Qiling(path, rootfs, ostype="linux", archtype="x86", verbose=QL_VERBOSE.DEBUG)
        ql.run()

    def shellcode(path, rtfs, shellcode):
        ql = Qiling(shellcoder=shellcode, rootfs=rtfs, ostype="linux", archtype="x86", output="disasm", verbose=QL_VERBOSE.DEBUG)
        ql.run()