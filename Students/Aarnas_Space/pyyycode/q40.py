a=input("enter the first number: ")
b=input("enter the second number: ")
c=input("enter the third number: ")
if int(a)<int(b) and int(a)<int(c) :
    print("the smaller number is... ",a)
elif int(b)<int(a) and int(b)<int(c) :
    print("the smaller number is ....",b)
else:
    print("the smaller number is ",c)