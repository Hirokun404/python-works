

import random

number = random.randrange(1,3)
userinput=int(input("enter number : "))
print("--------------------")

if userinput>number:
    print("your number is high")
elif userinput<number:
    print("your number is low")
else:
    print("correct answer")
print("--------------------")
print("computer number : ",number)
print("your number : ",userinput)



