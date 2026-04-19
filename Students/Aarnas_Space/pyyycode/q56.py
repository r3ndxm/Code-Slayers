#sum of all odd numbers from 1-n 
a=int(input("enter the value of the limit: "))
odd=0
i=1
for i in range(1,(a+1)):
    if i%2!=0:
        odd+=i
 

print("the sum of all the odd numbers are: ",odd)