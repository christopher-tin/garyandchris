tempResult = True
finalResult = False
n=2520

numbers = [11,13,14,15,16,17,18,19,20]

while finalResult == False:
    for number in numbers[::-1]:
        if n%number != 0:
            tempResult = False
            break
    if tempResult == False:
        n = n+2520
        tempResult = True
    else:
        finalResult = True
print(n)
