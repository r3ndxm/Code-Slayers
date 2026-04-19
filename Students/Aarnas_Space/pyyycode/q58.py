#numbers from 1-n that are multiple of 3

a = int(input("enter the value of the limit: "))
print(f"the multiples of three from 1- {a} are: ")
i=1
for i in range(1,a+1):
    if i%3==0:
     multiple=i     
     print(multiple)

