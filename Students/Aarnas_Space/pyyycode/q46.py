print("Calculating the sum of the first 5 natural numbers..")
e=input("do you wish to continue? type yes/no : ").lower()
if e=="yes":
 a=1 
 sum=0
 while a<6:
    sum= int(a)+sum
    a+=1
 print("the sum of the five natural numbers are...",sum)
else:
   print("_______end of program.______")