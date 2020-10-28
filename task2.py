#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

emptylist= []

word0= input("Enter a word: ").strip()
word1= input("Enter another word: ").strip()
word2= input("Enter one more word: ").strip()
word3= input("Enter another word: ").strip()
word4= input("Enter one last word: ").strip()

emptylist.insert(0, word0)
emptylist.insert(1, word1)
emptylist.insert(2, word2)
emptylist.insert(3, word3)
emptylist.insert(4, word4)

print(emptylist)