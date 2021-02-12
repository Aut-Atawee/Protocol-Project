import socket
import random
import json
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8009))
s.listen()

while True :

    try :
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
    except socket.error :
        print("Fail Connection")
        continue

    target_number = math.floor(random.random() * 100)
    
    receive = clientsocket.recv(1024)
    receive = json.loads(receive.decode("utf-8"))
    
    sendto_client = {
        "protocol" : "KFN" ,
        "status" : "787 Action" ,
        "message" : "Welcome " + receive["name"] + " to Koisuru Fortune Number!"
    }

    sendto_client = bytes(json.dumps(sendto_client),encoding="utf-8")
    clientsocket.send(sendto_client)

    while True :

        receive_from_client = clientsocket.recv(1024)
        data = json.loads(receive_from_client.decode("utf-8"))
    
        if data["guess"] < 0 or 100 < data["guess"] :
            sendto_client = {
                "protocol":"KFN",
                "status":"787 Action",
                "message":"Your guess is out of range, Please try again!"
            }
            sendto_client = bytes(json.dumps(sendto_client),encoding="utf-8")
            clientsocket.send(sendto_client)
        elif data["guess"] == target_number :
            sendto_client = {
                "protocol":"KFN",
                "status":"340 Close",
                "message":"Congratulations! Your guess is correct!"
            }
            sendto_client = bytes(json.dumps(sendto_client),encoding="utf-8")
            clientsocket.send(sendto_client) 
            break  
        elif data["guess"] > target_number :
            sendto_client = {
                "protocol":"KFN",
                "status":"787 Action",
                "message":"Your guess is too high, Please try again!"
            }
            sendto_client = bytes(json.dumps(sendto_client),encoding="utf-8")
            clientsocket.send(sendto_client)
        elif data["guess"] < target_number :
            sendto_client = {
                "protocol":"KFN",
                "status":"787 Action",
                "message":"Your guess is too low, Please try again!"
            }
            sendto_client = bytes(json.dumps(sendto_client),encoding="utf-8")
            clientsocket.send(sendto_client)
        else :
            sendto_client = {
                "protocol":"KFN",
                "status":"787 Action",
                "message":"Invalid input! Please input numeric 0-100"
            }
            sendto_client = bytes(json.dumps(sendto_client),encoding="utf-8")
            clientsocket.send(sendto_client)
    print("End connection")
    print()
    clientsocket.close()
clientsocket.close()