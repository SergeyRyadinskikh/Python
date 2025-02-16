# Ex_1 - receive 2 numbers from users input and print the greater number

"""
num1 = int(input("Enter first number > "))
num2 = int(input("Enter second number > "))
if num1 > num2:
    print (num1)
else:
    print (num2)
"""

# Ex_2 -receive string with preferred code language and if its not python, show user an error

"""
best_lang = "python"
inp1 = input("Enter best code language > ")
if inp1 == best_lang:
    print ("You guessed right :)")
else:
    print ("You are wrong, best language is Python.")
"""

# Ex_3 - receive 2 numbers from users input and compare their sum with fourth number.

"""
int1 = int(input("Enter first number > "))
int2 = int(input("Enter second number > "))
int3 = int1 + int2
print ("The summery of first and second number is {0}".format(int3))
int4 = int(input("Enter third number > "))
if int3 > int4:
    print("Well done, third number you entered is lower then sum of first two :) ")
elif int3 == int4:
    print("The numbers are equal :| ")
else:
    print("Wrong !!! You supposed to enter lower number then sum of first two numbers :(")
"""

# Ex_4 - append two new ports to consisting array.

"""
ports = [21,22,23,25]
print(ports)
new_port = int(input("Please add HTTP port number to the 'ports' list > "))
ports.append(new_port)
print(ports)
"""

# Ex_5 - ask for five numbers from user. Numbers must be between 1 and 5 and if they don`t, show error.
# In the end, if all numbers match the policy, print the list of numbers.


num_list = []

print("Please enter 5 numbers between 1 and 5")

for i in range(5):
    num1 = int(input("Enter a number >"))
    if 1 <= num1 <= 5:
        num_list.append(num1)
        summary = sum(num_list)
    else:
        print("Number you entered was NOT between 1 and 5 :(")
print("Numbers you entered: {0}".format(num_list))
print("The summary is: {0}".format(summary))


# Guessing game - Program makes every time random number, user must to guess the number. With every guess, program
# will show if the number users inserted is need to be higher or lower. In the end after user guesses the right
# number, program will show the random number and number of tries to guess.

"""
import random
print("Welcome to Guessing game, is this your first time ?")
options = input("To continue from last save [Y]es/[N]o ?")
if options == "y":
    with open("save.db","r") as fd:
        data = fd.read()
        data = data.split("|")
        rand = int(data[0])
        tries = int(data[1])
else:
    rand = random.randint(1,1000)
    tries = 0

while True:
    user_guess = input("What is the number [s]ave? > ")
    if user_guess == "s":
        with open("save.db","w") as fd:
            fd.write("{0}|{1}".format(rand, tries))
        exit(0)

    user_guess = int(user_guess)
    if user_guess == rand:
        break
    elif user_guess > rand:
        print("Your number is bigger")
        tries += 1
    else:
        print("Your number is lower")
        tries += 1
print("You win in {0} tries".format(tries))
"""

# Dictionary practice

"""
user = {"first_name":"Sergey","last_name":"Ryadinskikh","age":30,"state":"married"}
for key,value in user.items():
    print(key,value)
"""

# Functions practice, two ways >

"""
import functions

functions.welcome_page()
"""

"""
from functions import welcome_page

welcome_page()
"""

# Calculator (simple one)

"""
import functions

print("Welcome to Calculator")
num1 = int(input("Please enter FIRST number > "))
num2 = int(input("Please enter SECOND number > "))
operator = input("Please choose action: + or - or * or / ")

functions.calc1(num1,num2,operator)
"""

# Creating and writing inside new file

"""
file = open("test.txt","w")
file.write("Hello this is my first file")
file.close()
"""

# Reading from created file

"""
urls = []
file = open("readme.md.txt","r")
for link in file:
    if "http" in link:
        url = link[link.find("http"):-1]
        urls.append(url)
print(urls)
"""

"""
# Operating errors with all the options:

try:  # The main function
    number = int(input("Please enter your age >"))
except Exception as e:  # If there an error in main function then program saves it in error.log and proceeds to finally
    with open("error2.log","a") as fd:
        fd.write(str(e))
else:  # This function will be executed only if the main function worked, if there was an error it will jump to finally
    print("Your age is ",number)
finally:  # This function will be executed any way
    print("This is the program")
"""

# How to operate errors and save them to log file ("try" and "except") and if need how to read logfile

"""
try:
    num = int(input("Please enter number to divide > "))
    print (10/num)
except Exception as e:
    with open("error.log","a") as fd:
        fd.write(str(e)+"\n")
        print("You have an error, please check the log file.")
        filer = input("Would you like to open error log file [y]es or [n]o ?")
    if filer == "y":
        with open("error.log","r") as fd:
            data = fd.read()
            print(data)
else:
    exit(0)
"""

# How to open a file (choosing by name), and read it after that.

"""
try:
    filename = input("Please type the name of the file >")
    fd = open(filename,"r")
    print(fd.read())
except Exception as e:
    print("\n","There is no file with that name !","\n")
    print("Error is > ","\n",e)
else:
    fd.close()
finally:
    print("\n","Your logs are saved, good bye !")
    exit(0)
"""

# Modules,  first one is "os"

"""
import os

os.system("ipconfig")
"""

#

"""
import os

while True:
    command = input("type command, for exit type [exit] > ")
    if command == "exit":
        break
    else:
        print(os.popen(command).read())
"""

# Loop for CMD commands and special "ip" command to call function from another file

"""
import os,functions

commands = []
for i in range(3):
    command = input("type any CMD command, type exit to stop >")
    commands.append(command)
    if command == "exit":
        break
    elif command == "ip":
        res = functions.get_ip()
        print(res)
    else:
        print(os.popen(command).read())
        print("This is the commands you used >","\n",commands)
"""

# Program to ping websites with timer

"""
import time,os

start_time = time.time()
urls = ["www.google.com","www.facebook.com"]
for link in urls:
    os.system("ping {0}".format(link))
print(time.time() - start_time)
"""

# Threading module is used for running i/o data simultaneously

"""
import os,time,threading

def pinger(link):
    os.system("ping {0}".format(link))

start_time = time.time()
urls = ["www.google.com","www.facebook.com"]
threads = []

for link in urls:
    t = threading.Thread(target=pinger,args=(link,))
    threads.append(t)
    t.start()
for thread in threads:
    thread.join()
print(time.time() - start_time,urls)
"""

# Understanding of Threading, use threads to multitask hard drive processes (not effective with hard-drive).

"""
import time,threading

start_time = time.time()
threads = []

def counter(number):
   for i in range(number):
       print(i)
if __name__=='__main__':
    for i in range(5):
       t = threading.Thread(target=counter, args=(100000,))
       threads.append(t)
       t.start()
    for thread in threads:
        thread.join()
print(time.time() - start_time)
"""

# Understanding of MultiProcess, use "multiprocess" to multitask processor processes (effective).

"""
import time,multiprocessing

start_time = time.time()
processes = []

def counter(number):
    for i in range(number):
        print(i)
if __name__=='__main__':
    for i in range(5):
        p = multiprocessing.Process(target=counter,args=(100000,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
print(time.time() - start_time)
"""

# 1/2 Synchronization of threads, sliding processes multitasking ("Semaphore")

"""
import threading

processes = []

def counter(s):
    for i in range(100000):
        with s:
            print(i)
semaphore = threading.Semaphore(1)

if __name__=='__main__':
    for i in range(5):
        t = threading.Thread(target=counter,args=(semaphore,))
        processes.append(t)
        t.start()

"""

# 2/2 Synchronization of threads, sliding processes multitasking ("Lock")

"""
import threading

processes = []

def counter(s):
    for i in range(100000):
        with s:
            print(i)
lock = threading.Lock()

if __name__=='__main__':
    for i in range(5):
        t = threading.Thread(target=counter,args=(lock,))
        processes.append(t)
        t.start()
"""

# Socket building, how to open connection to your program

"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",1234))
server.listen(5)

input("Enter")
"""

# First Server with TCP connection (need client.py file)

"""
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 1234))
server.listen(5)

client, addr = server.accept()

print("Connected from {0}".format(addr))

while True:
    data = client.recv(2048).decode()
    print(data)
    if data == "exit":
        client.close()
        break
    client.sendall("Thanks".encode())
server.close()
"""
# Ex-1 Chat One-One (one client vs one server)

"""
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 1234))
server.listen(5)

client, addr = server.accept()

print("Connected from {0}".format(addr))

while True:
    data = client.recv(2048).decode()
    print(data)
    data2 = input("[+] Response >")
    client.sendall(data2.encode())
    if data == "exit":
        client.close()
        break
server.close()
"""

# Ex-2 Chat with multiply clients on the same server

"""
from socket import *
import threading

server = socket(AF_INET,SOCK_STREAM)
server.bind(("",4444))
server.listen(100)
print("Server started")

def chat(client):
    while True:
        data = client.recv(2048).decode()
        if data == "exit":
            client.close()
            break
        else:
            print(data)
            res = input("[+] Response >")
            client.sendall(res.encode())
    server.close()
while True:
    client, addr = server.accept()
    t = threading.Thread(target=chat,args=(client,))
    t.start()
"""

# Ex-3 Chat with multiply clients that can see all the massages, like WhatsUp

"""
from socket import *
import threading

def worker(client):
    while True:
        data = client.recv(2048).decode()
        if data == "exit":
            client.close()
            print("{0} disconnected".format(client))
            break
        for item in clients:
            item.sendall(data.encode())

server = socket(AF_INET,SOCK_STREAM)
server.bind(("",4444))
server.listen(100)
clients = []
print("Server started")

while True:
    client, addr = server.accept()
    clients.append(client)

    t = threading.Thread(target=worker,args=(client,))
    t.start()
"""

# Ex-4 Server that sends os.system commands to his clients and client sends response

"""
from socket import *
import threading

def worker(server):
    while True:
        client,addr = server.accept()
        clients.append(client)

server = socket(AF_INET,SOCK_STREAM)
server.bind(("",4444))
server.listen(100)
clients = []
print("Server started")

t = threading.Thread(target=worker, args=(server,))
t.start()

while True:
    data = input("Server command >")
    if clients:
        for client in clients:
            try:
                client.sendall(data.encode())
                result = client.recv(2048).decode()
                print(result)
            except:
                client.remove(client)
"""

# First scanning tool - scans for local ip addresses, 0.0.0.1 - 0.0.0.254

"""
from functions import *
import threading

threads = []
clients = []
my_ip = get_ip()
lan = my_ip[:my_ip.rfind(".")+1]
lock = threading.Lock()

for i in range(1,255):
    ip_addresses = lan+str(i)
    t = threading.Thread(target=scanner,args=(ip_addresses,clients,lock,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
print(clients)
"""

# Next exercise is the "Management Program". To see its source code, open project "Management Program".


# This is example to UDP Server with UDP client.

"""
from socket import *


server = socket(AF_INET, SOCK_DGRAM)
server.bind(("", 3333))

while True:
    print ("Waiting for connection")
    data, client = server.recvfrom(2048)
    print (data.decode())

    if data.decode() == "exit":
        server.close()
        break

    data = input("Server: ")
    server.sendto(data.encode(), client)
"""

# Learning Classes, first Company objects exercise - Romans version.

"""
class Employee(object):

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary(self):
        return "Your salary is {0}""\n".format(self.salary)

    def get_employee(self):
        print("\n""Hello {0} your position is {1} and your salary is {2}".format(self.name, self.position, self.salary))

    def update_salary(self, new_salary):
        self.salary = new_salary

    def update_position(self, new_pos):
        self.position = new_pos


emp1 = Employee("Sergey", "PenTester", 5000)
emp2 = Employee("Oleg", "DevOps", 10000)

while True:
    print("\n""This is Salary Management Program,choose an employee:\n1) Sergey Ryadinskikh\n2) Oleg Malinovski""\n")
    usr = int(input("Please enter user number of employee or type 0 to exit: > "))
    if usr == 1:
        emp1.get_employee()
        sal = emp1.get_salary()
        print(sal)
        new_sal = int(input("How much to update {0}`s salary ? > ".format(emp1.name)))
        if new_sal == "0":
            break
        else:
            emp1.update_salary(new_sal)
            emp1.get_employee()
        pos = input("Do you want to update your position ? y/n >")
        if pos == "y":
            new_pos = input("What is you new position >")
            emp1.update_position(new_pos)
            emp1.get_employee()
        else:
            continue
    elif usr == 2:
        emp2.get_employee()
        sal = emp2.get_salary()
        print(sal)
        new_sal = int(input("How much to update {0}`s salary ? > ".format(emp2.name)))
        if new_sal == "0":
            break
        else:
            emp2.update_salary(new_sal)
            emp2.get_employee()
        pos = input("Do you wont to update your position ? y/n >")
        if pos == "y":
            new_pos = input("What is you new position >")
            emp2.update_position(new_pos)
            emp2.get_employee()
        else:
            continue
    elif usr == 0:
        break
    else:
        print("Error, there is no such employee")
        exit(0)
"""




