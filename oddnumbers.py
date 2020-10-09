lower=int(input("enter lower limit for range"))
upper=int(input ("enter upper limit for range"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
