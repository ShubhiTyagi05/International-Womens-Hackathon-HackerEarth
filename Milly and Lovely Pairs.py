def countLowest(cuteList):
	count=0
	y=cuteList[0]
	for x in cuteList:
		if x==y:
			count=count+1
		else:
			break
	return count

def countHighest(cuteList):
	cuteList.reverse()
	count=0
	y=cuteList[0]
	for x in cuteList:
		if x==y:
			count=count+1
		else:
			break
	return count
		
def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0		

testCases = int(raw_input())
for x in range (0, testCases):
	num = long(raw_input())
	cuteList = raw_input().split()
	#print num
	cuteList = map(long, cuteList)
	#print cuteList
	cuteList.sort()
	if num>2:
		low = cuteList[0]
		high = cuteList[-1]
		countLow = countLowest(cuteList)
		countHigh = countHighest(cuteList)
		if low==high:
			print choose(num,2)
		else :
			print countLow*countHigh
	elif num==2:
		print 1
	else :
		print 0
		
		
	
