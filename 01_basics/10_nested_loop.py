# num=int(input("enter the number"))
# for j in range(1,num+1):
#     for i in range(1,j+1):   
#         print("*", end=)
#     print()

# for i in range(0,26):
#     print(chr(97+i))

# num=int(input("enter number"))
# for i in range(0,num):
#     for j in range(0,i+1):
#         print(chr(97+i),end="")
#     print()    

num=int(input("enter number"))
for i in range(0,num):
    for j in range(0,i+1):
        print(chr(97+j),end="")
    print()     

