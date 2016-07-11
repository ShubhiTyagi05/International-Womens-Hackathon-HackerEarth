testInfo = raw_input().split() 
n = int(testInfo[0]) 
x = int(testInfo[1]) 
testList = raw_input().split() 
testList = map(int, testList) 
count=0 
skipped = False 
for y in testList: 
	if y<=x: 
		count= count+1 
	elif skipped==False: 
		skipped=True 
		continue 
	else: 
		break 
print count   