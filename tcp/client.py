import socket
import sys
import os
    

def main():
    os.system("cls")
    ip = sys.argv[1]
    port = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    print(s.recv(1024).decode())

    done = False
    while not done:
        try:
            msg = input()
            s.send(msg.encode())
            if msg == "exit":
                print("Bye!")
                raise Exception()
            print(s.recv(1024).decode())
        except:
            print("Connection closed.")
            s.close()
            done = True

if __name__ == "__main__":
    main()
