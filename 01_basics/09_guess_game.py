import random
r=random.randint(1,100)
print("Let start the game you have only five chances:")
count=0;
for i in range(1,r+1):
    num=int(input("Guess the number :"))
    if num==r:
        print("Win",i)
        count+=1
        break
    elif num<r:
        print("your number is smaller, Try again")
        count+=1
    else:
        print("Your number is greater, Try again")
        count+=1
    if count==5:
        print("Failed , The number is :",r)
        break 
