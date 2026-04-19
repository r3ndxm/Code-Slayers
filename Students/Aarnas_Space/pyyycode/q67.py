#checking max for 5 integers
reset=0
for i in range(1,6):
    suffix=("th","st","nd","rd","th","th")[i%10]
    num=int(input(f"enter the {i}{suffix} integer"))
    if num>reset:
        reset=num
print("the maximum of the integers is ",reset)
 #checking max for n integers

n=int(input("enter the total number of integers: "))
for i in range(n):
    num4=int(input("enter the integer: "))
    if num4>reset:
        reset=num4
        
  
print("the maximum of the numbers is: ",reset)



