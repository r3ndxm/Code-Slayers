#sum of all even numbers from 1-n 
a=int(input("enter the value of the limit: "))
even=0
i=1
for i in range(1,(a+1)):
    if i%2==0:
        even+=i
    print("the sum of all the even numbers are: ",even)