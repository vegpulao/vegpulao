import random
from words import words
def win(s):
    print("YAAY you found the word",s)
def loose(s):
    print("BOO you lost the word was",s)
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
def wurd():
    word=random.choice(words).upper()
    while "-" in word or " " in word:
        random.choice(words).upper()
    return word
def hangman():
    guess=wurd()
    blank=""
    used=[]
    form=''
    lopez=''
    count=0
    jos=''
    print("This is your word")
    for x in guess:
        blank=blank+"_"
    blank=" ".join(blank)
    print(blank)
    blankl=list(blank.split(" "))
    while count<5:
        c=input("Enter an alphabet:").upper()
        if (c.isalpha()) and (len(c)==1) and (c not in used):
            if c in guess:
                for x in guess:
                    if x==c:
                        lal=findOccurrences(guess,x)
                        for i in lal:
                            blankl[i]=x
                jos=" ".join(form.join(blankl))
                print(jos)
            else:
                count=count+1
                match count:
                    case 1: print("x")
                    case 2: print("xx")
                    case 3: print("xxx")
                    case 4: print("xxxx")
        else:
            print("Please enter an alphabet or unused alphabet")
        for i in jos:
            if i != " ":
                lopez=lopez+i
        if lopez.isalpha():
            print(lopez)
            win(lopez)
            break
        lopez=''
        used.append(c)
    loose(guess)
hangman()
