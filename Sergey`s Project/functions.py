def welcome_page():
    print("Hello new user, please enter your first name > ")
    user = input(">")
    print("Welcome {0}".format(user))


# Calc with list

def calc1(num1, num2, operator):
    actions = ["+", "-", "*", "/"]
    while True:
        if operator == actions[0]:
            result = num1 + num2
        elif operator == actions[1]:
            result = num1 - num2
        elif operator == actions[2]:
            result = num1 * num2
        elif operator == actions[3]:
            result = num1 / num2
        print("The result is: {0}".format(result))
        break


# For first command program

def get_ip():
    import os
    output = os.popen("ipconfig")
    for address in output.readlines():
        if "IPv4 Address" in address:
            start = address.find(":")
            end = -1
            fin = address[start + 2:end]
            break
    return fin


# "get_ip2 try-on

def get_ip2():
    import os
    output = os.popen("ipconfig")
    for address in output.readlines():
        if "192.168.14" in address:
            start = address.find(":")
            end = -1
            fin = address[start + 2:end]
            print(fin)
            break


# Scanner N-1

def scanner(ip_address, clients, lock):
    import os
    result = os.popen("ping {0} -n 1".format(ip_address)).read()
    if "TTL" in result:
        with lock:
            print(ip_address)
            clients.append(ip_address)

