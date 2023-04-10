#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import speedtest
from threading import Thread
import time
import sys
import os

try:
    test = speedtest.Speedtest()

except:
    print("Could not connect to the internet...")
    exit()

string = "................"

def update():
	sys.stdout.write("\r")
	sys.stdout.flush()
	sys.stdout.write(" "*len(string))
	sys.stdout.flush()
	sys.stdout.write("\r")
	sys.stdout.flush()

def check(up, down):
    if down.is_alive() or up.is_alive():
        return True
    else:
        update()
        return False

def scroll_text(text, up, down):
    while check(up, down):
        for char in str(text):
            if check(up, down) == False:
                break
            sys.stdout.write(char)
            if check(up, down) == False:
                break
            time.sleep(.2)
            if check(up, down) == False:
                break
            sys.stdout.flush()
        update()

def go(up, down):
	scroll_text(string, up, down)

class Loading(Thread):
    def __init__(self, up, down):
        Thread.__init__(self)
        self.up = up
        self.down = down
    def run(self):
        go(self.up, self.down)

class Down(Thread):
    def run(self):
        tmp = round(test.download()/1000000, 2)
        update()
        print(f"Download Speed: {tmp} mbps")

class Up(Thread):
    def run(self):
        tmp = round(test.upload()/1000000, 2)
        update()
        print(f"Upload Speed: {tmp} mbps")

def main():
    up = Up()
    down = Down()
    load = Loading(up, down)
    os.system("clear")
    
    down.start()
    up.start()
    load.start()

if __name__ == "__main__":
    main()
