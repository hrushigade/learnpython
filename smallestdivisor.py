n=int(input("enter an integer"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("smallest divisor is",a[0])