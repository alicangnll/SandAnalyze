# SandAnalyze
Simulate Windows EXE for Malware Research!

<b>What is This ?</b>
<p>
SandAnalyze is a program that allows you to examine Windows EXE files on Linux with the help of GDB Debugger and perform operations on memory.
<br><br>
SandAnalyze, Linux üzerinde Windows EXE dosyalarını GDB Debugger yardımıyla inceleyebileceğiniz ve memory üzerinde işlem yapabileceğiniz bir programdır.
</p>

<br>
<img src="pic/test2.png" />
<br>

<b>Installation</b>
<pre>
pip install -r requirements.txt
Run dllscollector.bat
Create a folder inside of examples/rootfs/windows_xx/(folder name is bin)
Copy malware inside of examples/rootfs/windows_xx/bin
Run python_malwaresandbox.py
Example EXE name : example.exe
</pre>

<br>
<img src="pic/test1.png" />
<br>