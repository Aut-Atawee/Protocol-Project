import socket
import random
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 1234))
s.listen()

target_number = math.floor(random.random() * 100)
while True :
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    data = clientsocket.recv(1024)    
    clientsocket.sendall(bytes("Welcome " + str(data,"utf-8") +" to Koisuru Fortune Number!" ,"utf-8"))
    
    while True :

        guess_number = clientsocket.recv(1024)
        # clientsocket.send(bytes("Enter your guess (0-100) : " + clientsocket.recv(1024)), "utf-8")
        

        if (int.from_bytes(guess_number,byteorder="big") == target_number) :
            clientsocket.send(bytes("Congratulations!"+" Your guess is correct!","utf-8"))
            break
        elif int.from_bytes(guess_number,byteorder="big") > 100 or int.from_bytes(guess_number,byteorder="big") < 0 :
            clientsocket.send(bytes("Your guess is out of range","utf-8"))
        elif int.from_bytes(guess_number,byteorder="big") < target_number :
            clientsocket.send(bytes("Your guess is too low, Please try again!","utf-8"))
        elif int.from_bytes(guess_number,byteorder="big") > target_number :
            clientsocket.send(bytes("Your guess is too high, Please try again!","utf-8"))
    
    print("End")
    clientsocket.close()
clientsocket.close()