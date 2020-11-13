#! python3
"""
Ask the user to enter positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added


incorporate a while loop:
keep doing something until the entry is -1
add the new entry to a list


inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
lists= []
x=1

while x>=0:
    x= input("Enter an integer: ")
    x= int(x)
    if x<0:
        lists.sort()
        print("The largest number you entered is" + ' ' + str(lists[-1]))


    if x>0:
        lists.append(x)
        print(lists)





