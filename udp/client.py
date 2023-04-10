import socket

port = 9999
ip = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    _input = input()
    s.sendto(_input.encode(), (ip,port))
    if _input.lower() == "exit":
        print("Bye")
        s.close()
        break
    data = s.recvfrom(2048)
    print(data[0].decode())