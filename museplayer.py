import sys
from colorama import *
from playsound import playsound

#Music

#Arguments being given

print(Fore.YELLOW + "MusePlayer For Linux")

if len(sys.argv) == 2:
   File = sys.argv[1]
   print(Fore.GREEN + "Now playing from: {FileN}".format(FileN = File))
   print(Fore.WHITE + "Exit: CTRL + Z")

   playsound(File)

if len(sys.argv) == 3:
   File = sys.argv[1]
   File2 = sys.argv[2]
   print(Fore.GREEN + "Now playing from: {FileN}".format(FileN = File))
   print(Fore.GREEN + "Next in Queue: {File2N}".format(File2N = File2))
   print(Fore.WHITE + "Exit: CTRL + Z")

   playsound(File)
   playsound(File2)

#Error Handling

if len(sys.argv) < 2:
   print("MusePlayer Error: No Music File Specified")
