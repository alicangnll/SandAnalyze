import platform, unittest
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


class TestAndroid(unittest.TestCase):
    @unittest.skipUnless(platform.system() == 'Linux', 'run only on Linux')
    def test_android_arm64(self):
        test_binary = "examples/rootfs/arm64_android6.0/bin/arm64_android_jniart"
        rootfs = "examples/rootfs/arm64_android6.0"
        env = {
            'ANDROID_DATA': r'/data',
            'ANDROID_ROOT': r'/system'
        }

        ql = Qiling([test_binary], rootfs, env, profile={'OS64': OVERRIDES}, multithread=True)

        ql.os.set_syscall("close", my_syscall_close)
        ql.add_fs_mapper("/proc/self/task/2000/maps", Fake_maps(ql))
        ql.run()

        del ql

    @unittest.skipUnless(platform.system() == 'Linux', 'run only on Linux')
    def test_android_arm(self):
        test_binary = "examples/rootfs/arm64_android6.0/bin/arm_android_jniart"
        rootfs = "examples/rootfs/arm64_android6.0"
        env = {
            'ANDROID_DATA': r'/data',
            'ANDROID_ROOT': r'/system'
        }

        ql = Qiling([test_binary], rootfs, env, profile={'OS32': OVERRIDES}, multithread=True)

        ql.os.set_syscall("close", my_syscall_close)
        ql.add_fs_mapper("/proc/self/task/2000/maps", Fake_maps(ql))
        ql.run()

        del ql