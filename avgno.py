n=int(input("enter the number of elements to insert"))
a=[]
for i in range(0,n):
    elem=int(input("enter element"))
    a.append(elem)
avg=sum(a)/n
print("average of elements in list",round(avg,2))