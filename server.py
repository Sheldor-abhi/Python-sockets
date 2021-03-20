import socket

s = socket.socket()
s.bind(("localhost", 1235))
s.listen(0)
c, addr = s.accept()
while True:
    command= None
    print("Waiting for commands...")
    while command is None :
        command = c.recv(1024).decode()
    print("Command: ",command)
    #command execution part
    if command== "end" :
        break
    print("\n")
c.close()
