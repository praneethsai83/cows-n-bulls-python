import pandas as pd
import numpy as np
import random

words = pd.read_csv("words.csv")
w = np.array(words)

def cow_bull(guess,word):
    c,b = 0,0
    for i in range(0,4):
        for j in range(0,4):
            if(word[i] == guess[j] and i==j):
                b = b + 1
            elif(word[i] == guess[j] and i!=j):
                c = c + 1
    return c,b

word1 = str(w[random.randint(0,397)])
word = word1[2:6]

count = 1
print("Enter your gusses\n")
while(count <= 11):
    guess = input("Try " + str(count) + ": ")
    if(len(guess) != 4):
        print("Enter four letter word only!!")
    else:
        if(guess == word):
            print("You Won!!")
            break
        else:
            c,b = cow_bull(guess,word)
            print("c = ",c,"\nb = ",b)
            count = count + 1

if(count > 11):
    print("You Lost!!\nThe Word is " + word)
