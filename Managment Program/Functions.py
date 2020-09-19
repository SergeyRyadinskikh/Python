import os


def menu():
    print("""Welcome to Management Program, choose an option:
    1) Show all clients
    2) Execute command on client
    3) Shutdown client
    4) Type [exit] to close server and clients
    ---------------------------------------------------------""")


def get_all_clients(clients):
    counter = 0

    for client in clients:
        print("{0} : {1}".format(counter, client[1][0]))
        counter += 1


def command(clients):
    while True:
        get_all_clients(clients)
        try:
            client_id = int(input("Which client > "))
            client_socket = clients[client_id][0]
            command_execute = input("Enter a command: ")
            client_socket.sendall(command_execute.encode())
            result = client_socket.recv(2048).decode()
            print(result)
            break
        except:
            print("\n", "Numbers only !!!", "\n")
            continue


def shutdown(clients):
    while True:
        get_all_clients(clients)
        try:
            client_id = int(input("Which client > "))
            client_socket = clients[client_id][0]
            command_execute = os.popen("shutdown -s").read()
            client_socket.sendall(command_execute.encode())
            print("Command executed successfully !", "\n")
            break
        except:
            print("\n", "Numbers only !!!", "\n")
            continue
