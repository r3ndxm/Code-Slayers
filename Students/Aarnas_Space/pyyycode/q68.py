#checking min for 5 integers
reset= float("inf")
for i in range(1,6):
    suffix=("th","st","nd","rd","th","th")[i%10]
    num=int(input(f"enter the {i}{suffix} integer"))
    if num<reset:
        reset=num
print("the minimum of the integers is ",reset)
 #checking min for n integers
reset2=float("inf")
n=int(input("enter the total number of integers: "))
for i in range(n):
    num4=int(input("enter the integer: "))
    if num4<reset2:
        reset2=num4
        
  
print("the minimum of the numbers is: ",reset2)