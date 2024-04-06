from qiling import Qiling
from qiling.const import QL_VERBOSE
from qiling.exception import *

class QilingSandbox_Linux_X86_64:
    def test_elf_freebsd_asm(path, rootfs):     
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DUMP)
        ql.run()

    def test_elf_linux_arm_static(path, rootfs):     
        ql = Qiling(path, rootfs, verbose=QL_VERBOSE.DEFAULT)
        all_mem = ql.mem.save()
        ql.mem.restore(all_mem)
        ql.run()