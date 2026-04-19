b=input("enter a number ")
a=int(b)
print(f" the multiplication for {a} table is ....")
if a!=0:
    for i in range (1,11):
      
      table=int(a)*i
      print(f"{a}x{i}={table}")
else:
    print(" the number is invalid..")
