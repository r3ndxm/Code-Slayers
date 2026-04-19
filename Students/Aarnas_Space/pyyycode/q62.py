a=int(input("enter the number: "))
limit=int(input("enter the limit of the table: "))
if a!=0 and limit!=0 :
    i=0
    for i in range(1,limit+1):
        table=a*i
        print(f"{a} x {i} = ",table)
