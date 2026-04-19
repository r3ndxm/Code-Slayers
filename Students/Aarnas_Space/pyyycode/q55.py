#product of numbers from 1-n
n=int(input("enter the value of n: "))
i=1
product=1
for i in range(1,(n+1)):
 product *=i
 
print(f"the product of numbers from 1- {n} is ",product)