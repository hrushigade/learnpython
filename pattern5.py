n=7
px=1
for x in range(1,n+1):
	for y in range(1,n+1):
		if(y<=px or y>n-px+1):
			print("*",end="")
		else:
			print(" ",end=" ")
	if(x<=n/2):
		pre+=1
	else:
		px-1=1
		print()
