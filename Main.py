import ctypes
from pymem import Pymem
import pymem.process
import pymem
import tkinter.filedialog as filedialog
import PyBass.bass as b
def GetRustClientProcess():
    return Pymem("RustClient.exe")
def GetRust_ProcessHandle():
    return GetRustClientProcess().process_handle

def Main():
    b.BASS_INIT(device=-1, freq=44100, flags=0, win=0, dsguid=0)
    b.BASS_START()
    channelpl = b.BASS_StreamCreateFile(mem=0, filename="BringMeToLife.mp3".encode("UTF-8"), offset=0, length=0, flags=0x4)
    b.BASS_ChannelPlay(channelpl, False)
    pymem.disable_deprecated_warnings()
    filedll = filedialog.askopenfilename( title="Please Find DLL and Inject It!!!",filetypes=[("DLL Files", "*.dll")])
    pymem.process.inject_dll(GetRust_ProcessHandle(), filedll.encode("UTF-8"))
    exit(3329)

if __name__ == "__main__":
    Main()