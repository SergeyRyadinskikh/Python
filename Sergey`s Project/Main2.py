"""
from socket import *
from functions import *
import threading

clients = []

def sys_manager(server):
    while True:
        client, addr = server.accept()
        clients.append([client,addr])

server = socket(AF_INET,SOCK_STREAM)
server.bind(("",3333))
server.listen(100)

t = threading.Thread(target=sys_manager,args=(server,))
t.start()

while True:
    menu()
"""

# First Simple Network program

"""
from functions import *
import os

while True:
    scan = input("Please press [p] to PING Google or press [i] to check your IP Address, press [e]xit >")
    if scan == "p":
        res = os.popen("ping 8.8.8.8 -n 1").read()
        print("This is result: {0}".format(res))
    elif scan == "i":
        print("This is your IP Address:")
        get_ip2()
    elif scan == "e":
        break
    elif scan == "t":
        address = input("Please enter IP address to scan >")
        ping = os.popen("ping {0} -n 1".format(address)).read()
        print(ping)
"""












