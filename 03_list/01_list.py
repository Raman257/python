#properties of list
#ordered
#duplicates allowed
#hetrogeneous
#mutable
#are dynamic
#can be nested
#items can be accessed

#Create a list
L=[1,4,True,"Ram"]

#List vs Array
#dynamic size(list) vs Fixed size(Array)
#Hetrogenoues vs Homogeonous
#speed of exection is slow vs fast
#

# print(id(L))
# print(id(L[0]))
# print(id(L[1]))
# print(id(L[2]))
# print(id(L[3]))

# l=[]
# print("Enter values to make list")
# for i in range(0,4):
#     n=int(input("Press 1 for integer,Press 2 for String,Press 3 for boolean "))
#     if n==1:
#         l.append(int(input("Enter a interger")))
#     elif n==2:
#         l.append(input("Enter a string"))
#     else:
#         l.append(bool(input("Enter boolean value")))
# print(l)
# for j in range(0,4):
#     print(type(l[j]))

# l=[[[10,5],6,8],14,[4,6]]
# print(l)
# print(l[0][0][1])
# print(l[0][2])

l=[1,2,3,4,5]
print(l[::-1])


