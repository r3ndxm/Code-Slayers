#cube of numbers from 1-n
n=int(input("enter the value of the limit: "))
a=1
for a in range(1,(n+1)):
   cube=int(a)**3
   print(f"the cube of {a} is ",cube)