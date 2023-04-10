import socket
import subprocess

port = 9999
ip = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip,port))
print("Server is ready to receive message")
while True:
    message, client = server.recvfrom(2048)
    if message.decode().lower() == "exit":
        print("Client has disconnected from server")
        server.close()
        break
    mes = subprocess.getoutput(f"powershell.exe {message}")
    server.sendto(mes.encode(), client)