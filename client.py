import socket
c = socket.socket()
c.connect(("localhost", 1235))
while True :
    command=input("Enter command: ")
    print("Sending command...")
    c.send(bytes(command, "utf-8"))
    if command== "end" :
        break
    print("\n")
    
