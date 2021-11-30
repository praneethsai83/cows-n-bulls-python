# cows-n-bulls-python
Cows and Bulls is a word game wherein, based on some information given in the form of number of C's and B's, we need to guess the correct four letter word.

The game starts with a random guess of any meaningful four lettered word. The player will receive some information that would include the comparision between the correct word and the word entered.

C -> A 'C' implies that there is a letter which is common between the correct word and the word entered but its possition is not correct.
B -> A 'B' implies that there is a letter which is common between the correct word and the word entered and its possition is also correct.

For example:

#1
Let the correct word be 'BOAT'.
Let the word entered be 'LATE'.

In this case, both A and T are present in the correct word as well as the word entered but not at the correct possition so we would get 2C.

#2
Let the correct word be 'BOAT'.
Let the word entered be 'SOUP'.

In this case, only O is common in both the words so we would get 1B.

The player will get 11 chances to guess the correct word.
