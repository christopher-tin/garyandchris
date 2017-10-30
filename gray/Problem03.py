curVal = 2
primeVal = 1
newVal = 600851475143

while curVal <= newVal:
    if newVal % curVal == 0:
        primeVal = curVal
        newVal = newVal / primeVal
        curVal = 2
    else:
        if curVal <= 2:
            curVal += 1
        else:
            curVal += 2

print (primeVal) #max factor