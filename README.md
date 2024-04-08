# 🚀 SandAnalyze - Simulate Windows EXE on Linux / macOS!

<h2>❓What is This ?</h2>
<p>
<h3>ENGLISH</h3>
SandAnalyze is a program that allows you to examine Windows EXE files on Linux with the help of GDB Debugger and perform operations on memory.
<br><br>
<h3>TURKISH</h3>
<hr>
SandAnalyze, Linux üzerinde Windows EXE dosyalarını GDB Debugger yardımıyla inceleyebileceğiniz ve memory üzerinde işlem yapabileceğiniz bir programdır.
</p>

<br>
<img src="pic/test2.png" />
<br>

<h2>😎 Installation</h2>
<p>
<h3>ENGLISH</h3>
<br>
First, run the "dllscollector.bat" file on a Windows computer.
If the file you want to examine is 32 bit, copy the EXE file into the "examples/rootfs/x86_windows/bin" folder, if it is 64 bit, copy the EXE file into the "examples/rootfs/x8664_windows/bin" folder.
Then, run the "pip3 install -r requirements.txt" command on a Linux computer and install the Python PIP packages.
After all these procedures, you can start examining your EXE file with the "python3 example.py example.exe" command.
<br>
<h3>TURKISH</h3>
<br>
Öncelikle, Windows bir bilgisayar üzerinde "dllscollector.bat" dosyasını çalıştırın.
İncelemek istediğiniz dosya eğer 32 bit ise "examples/rootfs/x86_windows/bin" klasörü içerisine, 64 bit ise "examples/rootfs/x8664_windows/bin" klasörü içerisine EXE dosyasını kopyalayın
Ardından Linux bir bilgisayar üzerinden "pip3 install -r requirements.txt" komutunu çalıştırıp Python PIP paketlerini kurun.
Tüm bu işlemlerden sonra "python3 example.py example.exe" komutuyla EXE dosyanızı incelemeye başlayabilirsiniz.
</p>

<br>
<img src="pic/test1.png" />
<br>

<h2>📷 Video</h2>

<a href="https://github.com/alicangnll/SandAnalyze/blob/main/pic/installation.mp4">Installation</a>
<br>
<a href="https://github.com/alicangnll/SandAnalyze/assets/23417905/d91f09bb-c50c-4706-9489-fa96c72dec7f">Proof of Concepts</a>

<h2>NOTE </h2>
<p>
<b>UC_ERR_FETCH_UNMAPPED, UC_ERR_WRITE_UNMAPPED and related issues</b>

This is not a "bug". There are several possibilities why these errors occur.
<br>
1 - Windows API or syscall not being implemented
<br><br>
SandAnalyze with Qiling Framework tries to emulate various platforms such as <b>Linux, MacOS, Windows, FreeBSD and UEFI</b>. All these platforms come with different archnitecture. Its not possible for SandAnalyze with Qiling Framework to be able to emulate all these syscall/API. Community help is needed.
<br><br>
2 - Some specific requiremments are needed.
Firmware might need interface br0 and a users testing enviroment might not have it. In this case, ql.patch will come in handy.
<br><br>
3 - Required files are missing.
<br><br>
Missing conifig file or library can cause the targeted binary fail to run properly.
It is adviseble to always turn on debugging or disassambly mode to pintpoint the issue and try to resolve it. Technically, this is not a bug but rather a feature.
</p>
<br><br>
<b>Powered by <a href="https://docs.qiling.io/en/latest">Qiling Framework</a></b>
