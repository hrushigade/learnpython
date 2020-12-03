def insertionsort(nlist):
	for index in range(1,len(nlist)):
		currentvalue=nlist[index]
		position=index
		while(position>0 and nlist[position-1]>currentval
			nlist[position]=nlist[position-1]
			position=position-1
		nlist[position]=currentvalue
nlist=[14,46,43,27,57,41,21,70]
insertionsort(nlist)
print(nlist)