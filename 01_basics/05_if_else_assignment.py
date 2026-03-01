username="rony"
password="password"
u=input("Enter username:")
p=input("Enter password:")
if u==username and p==password:
    print("Valid User")
elif u!=username or p!=password:
    print("one entity is incorrect")
else:
    print("invalid user")    