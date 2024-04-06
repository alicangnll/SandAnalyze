#!/bin/bash
cp /usr/lib/dyld examples/rootfs/x8664_macos/usr/lib/;
cp /usr/lib/libSystem.B.dylib examples/rootfs/x8664_macos/usr/lib/;
cp /usr/lib/libc++.1.dylib examples/rootfs/x8664_macos/usr/lib/;
cp /usr/lib/libc++abi.dylib examples/rootfs/x8664_macos/usr/lib/;
cp /usr/lib/libobjc.A.dylib examples/rootfs/x8664_macos/usr/lib/;
cp -r /usr/lib/system examples/rootfs/x8664_macos/usr/lib/;
if [ -d /usr/lib/closure ]; then 
   cp -r /usr/lib/closure examples/rootfs/x8664_macos/usr/lib/;
fi

#if [ ! -d examples/rootfs/x8664_macos/System/Library/Kernels ]; then
#   mkdir -p examples/rootfs/x8664_macos/System/Library/Kernels;
#fi
#wget -O examples/rootfs/x8664_macos/System/Library/Kernels/kernel.development https://github.com/qilingframework/rootfs/raw/master/x8664_macos/System/Library/Kernels/kernel.development; 


#find /usr/lib -type d -exec mkdir -p examples/rootfs/x8664_macos{} \;
#find /usr/lib -type f -name "*.dylib" -not -name "libobjc.A.dylib" -exec install -v {} examples/rootfs/x8664_macos{} \;
