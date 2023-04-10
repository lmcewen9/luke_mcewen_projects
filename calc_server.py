import socket
import sys

try:
    ip = sys.argv[1]

except:
    try:
        ip = socket.gethostbyname(socket.gethostname())
        if ip == "127.0.0.1":
            raise Exception()
    except:
        from subprocess import getoutput
        from re import findall
        ifconfig = getoutput("ifconfig")
        lst = findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.(?!255)[0-9]{1,3}", ifconfig)
        ips = [x for x in lst if x != "127.0.0.1"]
        if (len(ips)) == 0:
            ip = "127.0.0.1"
        else:
            ip = ips[0]
            
port = 9999

def calculation(nums):
    try:
        total = float(nums[0])
    except:
        return "The first character has to be a number"
    for i in range(1,len(nums),2):
        try:
            prev_num = float(nums[i+1])
        except:
            return "Please make sure you are typing in a valid calculation..."
        i = nums[i]
        if i == "+":
            total += prev_num
        elif i == "-":
            total -= prev_num
        elif i == "*":
            total *= prev_num
        elif i == "%":
            try:
                total %= prev_num
            except:
                return "Can't modulo by 0..."
        else:
            try:
                total /= prev_num
            except:
                return "Can't divide by 0..."
            
    return total

def recieve(algo):
    nums = []
    num = ""
    for i in algo:
        if ord(i) >= 48 and ord(i) <= 57 or ord(i) == 46:
            num += i
        elif ord(i) == 42 or ord(i) == 43 or ord(i) == 45 or ord(i) == 47 or ord(i) == 37:
            nums.append(num)
            nums.append(i)
            num = ""
        elif ord(i) == 32:
            continue
        else:
            return "Please enter a valid symbol"
    nums.append(num)
    return calculation(nums)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    print(f"Hosting on {ip}:{port}")
    print("Calculator is listening...")

    client, address = server.accept()
    print(f"Client {address} has connected")
    client.send("\tWelcome to Calculator!\n".encode())
    
    done = False
    while not done:
        client.send("\nPlease enter a math problem: ".encode())
        data = client.recv(1024).decode().strip()
        if data.lower() == "exit":
            client.send("Goodbye!\n".encode())
            done = True
            server.close()
            print(f"Client {address} has disconnected")
        else:
            client.send(str(recieve(data)).encode())

if __name__ == "__main__":
    main()