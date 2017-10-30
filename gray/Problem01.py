countVar = 0
sumVar = 0 #storing our sum of multiples of 3 or 5

while (countVar < 1000):
    if (countVar % 3) == 0:
        sumVar = sumVar + countVar
    elif (countVar % 5) == 0:
        sumVar = sumVar + countVar
    countVar = countVar + 1
print (sumVar) 
