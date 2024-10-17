import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

class FunServer:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()
    
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input()
                    buffer += '\n'
                    self.socket.send(buffer.encod())
        except KeyboardInterrupt:
            self.socket.close()
            sys.exit()
    
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client, _ = self.socket.accept()
            client_thread = threading.Thread(target=self.handle, args=(client,))
            client_thread.start()
    
    def handle(self, client):
        if self.args.execute:
            output = execute(self.args.execute)
            client.send(output.encode())
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            with open(self.args.upload, 'wb') as file:
                file.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client.send(message.encode())
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client.send(b'#> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server killed {e}')
                    self.socket.close()
                    sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FunServer Net Tool", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''Example:
                                                                                                                            funserver.py -t 192.168.1.13 -p 9999 -l -c # command shell
                                                                                                                            funserver.py -t 192.168.1.13 -p 9999 -l -u=test.txt # upload file
                                                                                                                            funserver.py -t 192.168.1.13 -p 9999 -l -e=\"cat /etc/passwd\" # execute command
                                                                                                                            echo 'ABC' | ./funserver.py -t 192.168.1.13 -p 135 # echo text to server port 135
                                                                                                                                                    
                                                                                                                            funserver.py -t 192.168.1.13 -p 9999 # connect to server
                                                                                                                        '''))
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specific command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=9999, help='specified port')
    parser.add_argument('-t', '--target', default="127.0.0.1", help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    
    fs = FunServer(args, buffer.encode())
    fs.run()