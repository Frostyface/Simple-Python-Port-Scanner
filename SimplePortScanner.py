#!/bin/python3

'''
Port Scanner
'''

import socket
import subprocess
import sys
import pyfiglet
from datetime import datetime
from colorama import init, Fore

init()
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

#Clear Screen 
subprocess.call('cls', shell=True)

#Ask for input 
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(f"{RED}{ascii_banner}{RESET}")
print("-"*70)
print(f"Wait... Scanning remote host: {remoteServerIP}") 
print("-"*70)

#Check Date and Time Scan Starts
t1 = datetime.now()

try:
    for port in range(130,139):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))

        if result == 0:
            print(f"{GREEN}Port {port}:               OPEN{RESET}")
        sock.close()

except KeyboardInterrupt:
    print("Ctrl+C detected... Exiting...")
    sys.exit()

except socket.gainerror:
    print("Hostname could not be resolved... Exiting...")
    sys.exit()

except socket.error:
    print("Could not connect to server...")
    sys.exit()

#Check time again
t2 = datetime.now()
totaltime = t2 - t1
print(f"\n\nScannig Completed in {totaltime}")