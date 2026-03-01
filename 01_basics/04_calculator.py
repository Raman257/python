a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
print("For addition enter : +")
print("For subtraction enter : -")
print("For multiplication enter : *")
print("For division enter : /")
print("For floor division enter : //")
print("For mod enter : %")
op=input("Enter operation :")
if op=="+":
    print("Sum", a+b)
elif op=="-":
    print("Sub", a-b)
elif op=="*":
    print("mul", a*b)
elif op=="/":
    print("div", a/b)
elif op=="%":
    print("mod", a%b)
elif op=="//":
    print("floor div", a//b)
elif op=="**":
    print("power", a**b)
else :
    print("Invalid Input")