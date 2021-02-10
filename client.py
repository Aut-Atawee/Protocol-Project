import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1234))

name = input("Name : ")
s.send(bytes(name,"utf-8"))
data = s.recv(1024)
print(repr(str(data,"utf-8")))
while True :
    s.send(int(input()).to_bytes(2,byteorder="big"))
    data = s.recv(1024)
    print(repr(str(data,"utf-8")))
    if ((str(data,"utf-8")) == "Congratulations! Your guess is correct!") :
        break
s.close()
print('End')