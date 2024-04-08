import platform, unittest, shutil, os
from collections import defaultdict
from qiling import Qiling
from qiling.os.mapper import QlFsMappedObject
from qiling.os.posix import syscall


class Fake_maps(QlFsMappedObject):
    def __init__(self, ql: Qiling):
        self.ql = ql

    def read(self, size):
        return ''.join(f'{lbound:x}-{ubound:x} {perms}p {label}\n' for lbound, ubound, perms, label, _ in self.ql.mem.get_mapinfo()).encode()

    def fstat(self):
        return defaultdict(int)

    def close(self):
        return 0


def my_syscall_close(ql: Qiling, fd: int) -> int:
    if fd in (0, 1, 2):
        return 0

    return syscall.ql_syscall_close(ql, fd)

OVERRIDES = {'mmap_address': 0x68000000}
env = {
    'ANDROID_DATA': r'/data',
    'ANDROID_ROOT': r'/system'
    }


class TestiOS(unittest.TestCase):
    @unittest.skipUnless(platform.system() == 'Linux', 'run only on Linux')
    def test_ios_arm64(exeloc):
        if os.path.exists("examples/rootfs/arm64_ios/bin") is False:
            os.mkdir("examples/rootfs/arm64_ios/bin")
        
        shutil.copyfile("exefiles/" + exeloc, "examples/rootfs/arm64_ios/bin/" + exeloc)

        ql = Qiling(["examples/rootfs/arm64_ios/bin/" + exeloc], "examples/rootfs/arm64_ios", env, profile={'OS64': OVERRIDES}, multithread=True)
        ql.os.set_syscall("close", my_syscall_close)
        ql.add_fs_mapper("/proc/self/task/2000/maps", Fake_maps(ql))
        ql.run()
        del ql

    @unittest.skipUnless(platform.system() == 'Linux', 'run only on Linux')
    def debug_ios_arm64(exeloc, debugger):
        if os.path.exists("examples/rootfs/arm64_ios/bin") is False:
            os.mkdir("examples/rootfs/arm64_ios/bin")
        
        shutil.copyfile("exefiles/" + exeloc, "examples/rootfs/arm64_ios/bin/" + exeloc)

        ql = Qiling(["examples/rootfs/arm64_ios/bin/" + exeloc], "examples/rootfs/arm64_ios", env, profile={'OS64': OVERRIDES}, multithread=True)
        ql.os.set_syscall("close", my_syscall_close)
        ql.add_fs_mapper("/proc/self/task/2000/maps", Fake_maps(ql))
        ql.debugger = str(debugger)
        ql.run()
        del ql