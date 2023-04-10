import socket
import subprocess


def recieve(server):
    client, address = server.accept()
    print(f"Client connected with {str(address)}")
    client.send("Welcome to Server!".encode())
    done = False
    while not done:
        data = client.recv(1024).decode()
        if data == "exit":
            print("Client has disconnected")
            done = True
            server.close()
        try:
            out = subprocess.getoutput(f"powershell.exe {data}")
            if out == "":
                raise Exception()
            client.send(out.encode())
        except:    
            client.send("Invalid command".encode())

def main():
    ip = "127.0.0.1"
    port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    print("Server is listening...")
    recieve(server)


if __name__ == "__main__":
    main()