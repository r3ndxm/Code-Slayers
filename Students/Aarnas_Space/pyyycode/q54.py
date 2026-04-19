#sum of numbers from a-b(inclusive)
a=int(input("enter the first number to begin: "))
b=int(input("enter the last number of the series:"))
sum=0
i=a
for i in range(a,b+1):
    sum +=i
    
print("the sum of the series entered is ",sum) 