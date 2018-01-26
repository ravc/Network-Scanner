import os
import time

def TXT(file_name, content):
    w = open(file_name, 'a')
    w.write(content)
    w.close()

whitelist = []

logged = []

IPS = input('Input start IP address: ')
IPE = input('Input end IP address: ')
Loop = input('Loop the scan? ')
IP = IPS.split('.')
IP2 = IPE.split('.')
IP3 = IP[-1]

if Loop == 'y':
    while True:
        for i in range(int(IP[-1]), int(IP2[-1])+1):
            IP = '.'.join(IP)
            response = os.system('ping -c 1 ' + IP + ' > /dev/null')
            if response == 0:
                print(IP + ' is up')
                TXT('nscan.txt', IP + ' is up')
            else:
                print(IP + ' is down')
                TXT('nscan.txt', IP + ' is down')
            IP = IP.split('.')
            IP[-1] = str(int(IP[-1]) + 1)
        IP[-1] = IP3
elif Loop == 'n':
    for i in range(int(IP[-1]), int(IP2[-1])+1):
        IP = '.'.join(IP)
        response = os.system('ping -c 1 ' + IP + ' > /dev/null')
        if response == 0:
            print(IP + ' is up')
            TXT('nscan.txt', IP + ' is up')
        else:
            print(IP + ' is down')
            TXT('nscan.txt', IP + ' is down')
        IP = IP.split('.')
        IP[-1] = str(int(IP[-1]) + 1)
else:
    print('Not a valid input')
