#square of numbers from 1-n
n=int(input("enter the value of the limit: "))
a=1
for a in range(1,(n+1)):
   square=int(a)**2
   print(f"the square of {a} is ",square)