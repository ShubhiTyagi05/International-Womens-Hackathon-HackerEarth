def leftRotation(l,num):
	num = num % len(l)
	return l[num:]+l[:num]

def rightRotation(l,num):
	num = num % len(l)
	return l[-num:]+l[:-num]
	
nm = raw_input().split()
n = long(nm[0])
m = long(nm[1])
listA = raw_input().split()
listA= map(long,listA)
targetList = raw_input().split()
targetList = map(long,targetList)
count=0
achieved = False
if n<2 or len(listA)!=len(targetList):
	print -1
else:
	for x in range(0,m):
		operation = raw_input().split()
		num = long(operation[1])
		direction = operation[0]
		if direction=='L':
			if num%len(listA)!=0:
				listA = leftRotation(listA,num)
			#listA = np.roll(listA,-1*num)
			count = count+1
		elif direction=='R':
			if num%len(listA)!=0:
				listA= rightRotation(listA,num)
			#listA = np.roll(listA,num)
			count=count+1
		if listA==targetList:
			print count
			achieved=True
			break
	if achieved==False:
		print -1
		
