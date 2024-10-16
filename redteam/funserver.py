import socket

def recieve(server):
    client, address = server.accept()
    print(f"Client connected with {str(address)}")
    done = False
    while not done:
        print(client.recv(1024).decode())
        try:
            server.settimeout(30)
            msg = input()
            if msg == "exit":
                raise KeyboardInterrupt
            client.send(msg.encode())
        except TimeoutError as _:
            client.send("ls".encode())
        except KeyboardInterrupt as _:
            print("Goodbye!")
            client.close()
            server.close()
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen()
    print("Server is listening...")
    recieve(server)

if __name__ == "__main__":
    main()