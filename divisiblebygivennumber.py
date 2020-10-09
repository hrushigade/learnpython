lower=int(input("enter lower range limit"))
upper=int(input("enter upper range limit"))
n=int(input("enter the no to be divided"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)