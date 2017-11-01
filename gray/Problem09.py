def sumOfTriple(sumVal):
    for a in range (1,sumVal):
        for b in range (1,sumVal):
            c = (sumVal - a - b)
            if (a*a + b*b) == (c*c):
                #a,b,c
                return a,b,c
            b += 1
        a += 1

print (sumOfTriple(1000))