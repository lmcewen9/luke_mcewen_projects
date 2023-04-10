import random
#import enchant

KEY_WORDS = ["the", "would", "for", "this", "that", "them", "have", "with", "you", "but", "from", "going", "like"]

def position_letter(letter,position):
    upper = False
    if letter.isupper() == True:
        upper = True
    elif position > 26:
        position = position %26
    letter = letter.lower()
    if letter.isalpha() == False:
        return letter
    elif ord(letter) + position > 122:
        excess = (ord(letter) + position) - 122
        if upper == True:
            change = chr(96 + excess)
            return change.upper()
        return chr(96 + excess)
    elif upper == True:
        upper_shift = ord(letter) + position
        return chr(upper_shift).upper()

    shift = ord(letter) + position
    return chr(shift)

def random_position():
    return random.randint(1,25)

def check_string(string):
    for i in range(len(KEY_WORDS)):
        if KEY_WORDS[i] in string.lower():
            return True
    return False

def build_cipher(string, position_move=random_position()):
    ceaser = ""
    for i in string:
        ceaser += position_letter(i,position_move)
    return ceaser

def break_cipher(string):
    decrypts = set()
    for i in range(1,26):
        decrypt = ""
        for k in string:
            if k.isupper():
                decrypt += position_letter(k, i)
            else:
                decrypt += position_letter(k, i)
        decrypts.add(decrypt)
        if check_string(decrypt):
            print("Number of position switches:", i)
            return decrypt
        else:
            continue
    print("Couldn't find correct string, do any of these make sense?:")
    return decrypts

def main():
    build = input("Please type something you would like to encrypt: ")
    '''position_swap = input("How many positions would you like your string to be swithced by? (press enter to choose a random amount): ")
    if position_swap == "":
        position_swap = random_position()'''
    encrypt = build_cipher(build)
    print(encrypt)
    decrypt = input("Would you like to decrypt your string? (y/n): ")
    if decrypt.lower() == "y":
        print(break_cipher(encrypt))
    else:
        print("Okay here is your encrypted string", encrypt)

if __name__ == "__main__":
    main()