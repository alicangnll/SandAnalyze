import platform, unittest
from qiling import *
from qiling.os.posix import syscall
from qiling.os.mapper import QlFsMappedObject
from collections import defaultdict

class Fake_maps(QlFsMappedObject):
    def __init__(self, ql):
        self.ql = ql
    def read(self, size):
        stack = next(filter(lambda x : x[3]=='[stack]', self.ql.mem.map_info))
        return ('%x-%x %s\n' % (stack[0], stack[1], stack[3])).encode()
    def fstat(self):
        return defaultdict(int)
    def close(self):
        return 0
    
class QilingForAndroid():
     @unittest.skipUnless(platform.system() == 'Linux', 'run only on Linux')
     def my_syscall_close(ql, fd):
        if fd in [0, 1, 2]:
            return 0
        return syscall.ql_syscall_close(ql, fd)

     def test_android_arm64(self):
        test_binary = "../examples/rootfs/arm64_android6.0/bin/arm64_android_jniart"
        rootfs = "../examples/rootfs/arm64_android6.0"
        env = {"ANDROID_DATA":"/data", "ANDROID_ROOT":"/system"}

        ql = Qiling([test_binary], rootfs, env, multithread=True)
        ql.os.set_syscall("close", QilingForAndroid.my_syscall_close)
        ql.add_fs_mapper("/proc/self/task/2000/maps", Fake_maps(ql))
        ql.run()