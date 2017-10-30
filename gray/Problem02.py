fibA = 0
fibB = 1
fibFinal = 0
sumVar = 0

while fibFinal <= 4000000:
    fibFinal = fibA + fibB
    if fibFinal % 2:
        sumVar = sumVar
    else:
        sumVar = sumVar + fibFinal
    fibA = fibB
    fibB = fibFinal

print (sumVar)
