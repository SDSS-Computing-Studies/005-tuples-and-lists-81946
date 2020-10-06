#! python3
"""
Ask the user to enter positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

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
a=1


one= input("Enter an integer: ")
one= int(one)
if one>0:
    lists.append(one)
    a=a+1





if a==2:
    two= input("Enter an integer: ")
    two= int(two)
    if two>0:
        lists.append(two)
        a=a+1



if a==3:
    three= input("Enter an integer: ")
    three= int(three)
    if three>0:
        lists.append(three)
        a=a+1



if a==4:
    four= input("Enter an integer: ")
    four= int(four)
    if four>0:
        lists.append(four)
        a=a+1
   


if a==5:
    five= input("Enter an integer: ")
    five= int(five)
    if five>0:
        lists.append(five)
        a=a+1



if a==6:
    six= input("Enter an integer: ")
    six= int(six)
    if six>0:
        lists.append(six)
        a=a+1



if a==7:
    seven= input("Enter an integer: ")
    seven= int(seven)
    if seven>0:
        lists.append(seven)
        a=a+1

  

if a==8:
    eight= input("Enter an integer: ")
    eight= int(eight)
    if seven>0:
        lists.append(eight)
        a=a+1






lists.sort()
print(lists)

if a==1:
    print( lists[0] )
if a==2:
    print( lists[1] )
if a==3:
    print( lists[2] )
if a==4:
    print( lists[3] )
if a==5:
    print( lists[4] )
if a==6:
    print( lists[5] )
if a==7:
    print( lists[6] )
if a==8:
    print( lists[7] )

