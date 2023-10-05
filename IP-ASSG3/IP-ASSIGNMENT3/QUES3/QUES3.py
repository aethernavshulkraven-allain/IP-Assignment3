import random
import re
#For user to input
n = int(input("Enter the number of students/files: "))
files = []
out = open("QUES3/scores.txt", "w")
for i in range(n):
    files.append(open(input("Enter the address of file: "), "r"))

def totalWrd(x):
    global files
    ans = len(files[x-1].read().split())
    files[x-1].seek(0, 0)
    return ans

def uniqueWrd(x):
    uniq = []
    for l in files[x-1]:
        for j in l.split():
            j = j.lower()
            j = re.sub(r'[^\w\s]', '', j)
            if j not in uniq: uniq.append(j)
    files[x-1].seek(0, 0)
    return len(uniq)

def f1(x):
    return uniqueWrd(x)/totalWrd(x)

def freqCounter(x):
    freq = {}
    for l in files[x-1]:
        for wrd in l.split():
            wrd = wrd.lower()
            wrd = re.sub(r'[^\w\s]', '', wrd)
            if wrd not in freq.keys(): freq[wrd] = 1
            else: freq[wrd] += 1
    sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
    files[x-1].seek(0, 0)
    return dict(sorted_freq)

def f2(x):
    if len(freqCounter(x).keys()) >= 5:
        tot = sum(list(freqCounter(x).values())[:5])
        return tot/totalWrd(x)
    else:
        tot = sum(list(freqCounter(x).values())[:])
        return tot/totalWrd(x)

def f3(x):
    sent = 0
    spl_sent = 0
    s = files[x-1].read().replace("\n", "")
    for i in s.split("."):
        i = re.sub(r'[^\w\s]', '', i)
        if len(i)>0: sent += 1
        if (len(i.split())>35 or len(i.split())<5) and bool([x for x in i.lower() if x in "abcdefghijklmnopqrstuvwxyz"]): spl_sent += 1
    files[x-1].seek(0, 0)
    return spl_sent/sent

print(f3(1))

def f4(x):
    punc = ".,;:-"
    cons_punc = 0
    s = files[x-1].read().replace("\n", "")
    i = 0
    while(i<=len(s) - 2):
        if s[i] in punc and s[i+1] in punc:
            for j in range(i+2, len(s) - 1):
                if s[j] not in punc:
                    cons_punc += 1
                    i = j
                    break
                else: continue
        i += 1
    files[x-1].seek(0, 0)
    return cons_punc/totalWrd(x)

def f5(x):
    return 1 if totalWrd(x)>750 else 0


for i in range(n):
    score = 4 + f1(i+1)*6 + f2(i+1)*6 -f3(i+1) - f4(i+1) - f5(i+1)
    out.write("file"+str(i+1)+"\n")
    out.write("Scores: " + str(score) + "\n")
    out.write("five most used words in descending order: " + str(list(freqCounter(i+1).keys())[0:5]) + "\n")
    l = []
    ct = 0
    if len(freqCounter(i+1).keys())>=5:
        while(ct<5):
            t = random.randint(0, len(freqCounter(i+1).keys()))
            if t not in l:
                l.append(list(freqCounter(i+1).keys())[t])
                ct += 1
            else: t = random.randint(0, len(freqCounter(i+1).keys()))

    else: l = list(freqCounter(i+1).keys())

    out.write("5 random words from the submission are: " + str(l) +"\n")
    out.write("--------------------\n")