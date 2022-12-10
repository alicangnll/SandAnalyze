from qiling import Qiling
from qiling.const import QL_VERBOSE
from qiling.exception import *

class QilingSandbox_Linux:
    def test_elf_freebsd_asm(path, rootfs):     
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DUMP)
        ql.run()

    def test_libpatch_elf_linux_x8664(path, rootfs):
        ql = Qiling(path, rootfs)
        ql.patch(0x0000000000000575, b'qiling\x00', target='libpatch_test.so')
        ql.run()
        
    def test_elf_linux_x86(path, rootfs, filename = 'test.qlog'):
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DEBUG, log_file=filename)
        ql.run()

    def test_elf_linux_arm_static(path, rootfs):     
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DEFAULT)
        all_mem = ql.mem.save()
        ql.mem.restore(all_mem)
        ql.run()

    def shellcode(path, rtfs, shellcode):
        ql = Qiling(shellcoder=shellcode, rootfs=rtfs, ostype="linux", archtype="x86", output="disasm")