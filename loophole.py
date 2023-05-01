#!/usr/bin/python3 -tt

#########################################################
#                                                       #
#  THIS WAS ORIGINAL CODE. NOW OPTIMIZED FOR BETTER UI  #
#                                                       #
#  #START_SCAN                                          #
#     result = s.connect_ex((target, port))             #
#     print(port)                                       #
#     if result == 0:                                   #
#         print("[*] Port {} is open!".format(port))    #
#         s.close()                                     #
#                                                       #
#########################################################

# IMPORT_PACKAGES:
import sys
import time
import socket
import argparse
from tqdm import tqdm
from colorama import *
import pyfiglet as fig

# SETUP_TOOL:
initialise

banner = fig.figlet_format("loophole!")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(0.5)
time = time.asctime()

# PRINT_BANNER:
print(Back.LIGHTBLACK_EX, "Hello! Welcome to:", Back.RESET, ' ')
print(Fore.GREEN, banner, Fore.RESET, Back.LIGHTBLACK_EX, " " * 25, "@tehmasta", Back.RESET)
print(' ')

# COLLECT_IP:
target = input(str("Please enter your target's IP address: "))

# SHOW_PROGRESS:
print('*' * 50)
print(Fore.RED, Back.WHITE, 'Scanning target:   ', Fore.WHITE, Back.RED, target, Fore.RESET, Back.RESET)
print(Fore.RED, Back.WHITE, 'Starting time:     ', Fore.WHITE, Back.RED, time, Fore.RESET, Back.RESET)
print('*' * 50)

# START_SCAN
total_ports = 65535
bar_format = "{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"
bar = tqdm(total=total_ports, bar_format=bar_format, ncols=80, desc='Scanning Ports', position=0, leave=True, file=sys.stdout)
open_ports = []

def scan():
    try:
        for port in tqdm(range(1, total_ports+1)):
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
        s.close()
    except Exception as e:
        print(Fore.RED, "Scan has failed:", f"\n {e}", Fore.RESET)
        exit()
scan()

# FINISH_SCAN//CLOSE_PROGRESS_BAR

if not scan():
    if open_ports:
        print(Fore.GREEN, "Scan Complete!", Fore.WHITE, "\n", "-" * 50)
        for port in open_ports:
            print(Fore.LIGHTGREEN_EX, "\U0001F480", "Port {} is open!".format(port))
    else:
        print(Fore.RED, "No open ports found.")
        
# # WARNING: NOT RESETTING THIS WILL COLOR STDOUT PERMANENTLY!: # #
print(Fore.RESET)
