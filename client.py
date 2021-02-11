import socket
import json
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.connect(("localhost", 8009))
except socket.error :
    print("Fail Connection")
    sys.exit()

name = input("Enter your name : ")
data = {
    "protocol":"KFN",
    "status":"747 Hello",
    "name":name
}
data = bytes(json.dumps(data),encoding="utf-8")
s.send(data)

while True :

    receive = s.recv(1024)
    receive = json.loads(receive.decode("utf-8"))
    print(receive["message"])

    if receive["status"] == "350 Again" :
        guess = int(input("Enter your guess (0-100) : "))
        sendto_server = {
            "protocol":"KFN",
            "status":"747 Guess",
            "guess":guess
        }
        sendto_server = bytes(json.dumps(sendto_server),encoding="utf-8")
        s.send(sendto_server)
    elif receive["status"] == "340 Close" :
        print("End connection")
        s.close()
        break