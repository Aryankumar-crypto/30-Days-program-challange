import random
Cnumber=random.randrange(1,101)
Usernumber=int(input("Enter a number :--"))
if Usernumber>Cnumber:
    print("Computer number",Cnumber)
    print("Your guess number is too high..")
elif Cnumber>Usernumber:
    print("Computer number",Cnumber)
    print("Your guess number is too low..")  
else:
    print("Computer number",Cnumber)
    print("your guess number is equal..")      