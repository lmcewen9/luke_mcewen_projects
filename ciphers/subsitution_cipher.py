import random

ENCRYPT_MAP = {}
DECRYPT_MAP = {}

rand = random.Random()
for i in range(58, 127):
    randomNum = rand.randint(58, 126)
    done = False
    while not done:
        if chr(randomNum) not in DECRYPT_MAP.keys():
            ENCRYPT_MAP[chr(i)] = chr(randomNum)
            DECRYPT_MAP[chr(randomNum)] = chr(i)
            done = True
        else:
            randomNum = rand.randint(58, 126)

def encrypt(plaintext):
    s = ""
    for i in range(len(plaintext)):
        s += ENCRYPT_MAP.get(plaintext[i])
    return s

def decrypt(encrypted_text):
    s = ""
    for i in range(len(encrypted_text)):
        s += DECRYPT_MAP.get(encrypted_text[i])
    return s

def main():
    done = False
    while not done:
        plaintext = input("What would you like to encrypt?: ")
        encrypted_text = encrypt(plaintext)
        print(encrypted_text)
        yesornoDecrypt = input("Would you like to ao decrypt your text or exit? y/n/exit: ")
        if yesornoDecrypt.strip().lower() == 'y':
            print(decrypt(encrypted_text))
        elif yesornoDecrypt.strip().lower() == 'n':
            break
        elif yesornoDecrypt.strip().lower() == "exit":
            done = True
        else:
            print("Not a valid command")

if __name__ == "__main__":
    main()
