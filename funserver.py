import socket

def recieve(server):
    client, address = server.accept()
    print(f"Client connected with {str(address)}")
    done = False
    while not done:
        print(client.recv(1024).decode())