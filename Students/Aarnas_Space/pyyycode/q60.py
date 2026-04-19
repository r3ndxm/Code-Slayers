#numbers from 1-n that are multiple of 5 and 3
a=int(input("enter the value of the limit: "))
f=0
i=1
print("the multiples of 3 and 5 are: ")
for i in range(1,(a+1)):
    if i%3==0 and i%5==0 :
      multiple=i
      print(multiple)
