#print lenght of string without using len function
# str=input("enter string : ")
# count=0
# for i in str:
#     count+=1
# print("length of string is ",count)    

#print only username in email id
# email=input("Enter email id : ")
# print("username is : ",end="")
# for i in email:
#     if i=="@":
#         break
#     print(i,end="")

#count character in string according to user
str=input("Enter string : ")
ch=input("Enter character : ")
count=0
for i in str:
    if i==ch:
        count+=1
print(count)        

    