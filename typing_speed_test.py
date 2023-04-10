import time
from random import randint

sentences = [
            "Luke is the best and there is nothing anyone can tell him because he is amazing and the best and no one else compares in the slightest",
            "How much wood could a woodchuck chuck if a woodchuck could chuck wood",
            "Morrgan sells seashells on the seashore mostly due to the fact that she is on the beach and does not have anything else to do with her time",
            "Chemistry is the worst yeah chemistry is the worst say it with me now chemistry is the worst we all hate it and no one wants to be here but I am lowkey excited for lab tonight",
            "I can not think of another sentence so here we are just me rambling on and on with no idea where I am going with this the kid in front of me has a really big laptop and he does not rock with computers how lame but he got it at a good price so good for him I guess okay I am ready to end the sentence now"
            ]
sentence = sentences[randint(0, len(sentences)-1)]

def add_to_dic(lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    return dic

def check(_input):
    tmp = sentence.split(" ")
    sen = add_to_dic(tmp)
    user = add_to_dic(_input.split(" "))
    total_right = 0

    for i in sen:
        try:
            if sen[i] == user[i]:
                total_right+=sen[i]
            elif sen[i] > user[i]:
                total_right += user[i]
        except:
            pass
    
    return str(round(total_right/len(tmp)*100, 3)) + "%"

def main():
    print("\tWelcome to the typing speed test!!\n")
    time.sleep(1)
    print("Get ready for your prompt...\n")
    time.sleep(2)
    start = time.perf_counter()
    print(sentence+"\n")
    msg = input()
    stop = time.perf_counter()
    error = check(msg)
    t = stop-start
    wpm = round(len(msg.split())* (60/t), 2)
    print(f"\nYou typed {wpm} wpm with {error} correctness")


if __name__ == "__main__":
    main()