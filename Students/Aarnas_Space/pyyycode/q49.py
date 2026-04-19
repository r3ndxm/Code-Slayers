print("Calculating the sum of the even integers..")
b=int(input("enter the value of n "))
print("the limit you have entered is ",b)
e=input("do you wish to continue? type yes/no : ").lower()
if e=="yes":
 sum=0
 a=0
 while a<(b+1):
    if a%2==0 :
     sum= int(a)+sum
    a+=1
 print("the sum of the even natural numbers entered are...",sum)
else:
   print("_______end of program.______")
