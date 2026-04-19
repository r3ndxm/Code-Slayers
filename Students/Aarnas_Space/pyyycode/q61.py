a=int(input("enter the number:"))
if a!=0 :
    print("the multiplication of the number is:")
    i=0
    for i in range(1,11):
     table=a*i
     print(f"{a} x {i} = ",table)