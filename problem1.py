#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""

lists= ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']

print(lists)
word1= input("Choose a person from the list to replace: ")
word2= input("Enter the replacement: ")

whereword1 = lists.index(word1)

lists.remove(word1)

lists.insert(whereword1, word2)

print(lists)