tempResult = False
finalResult = False

n = 5
numbers = [2,3]
while len(numbers) < 10001:
    for number in numbers:
        if n%number == 0:
            tempResult = True
            break
    if tempResult == False:
        numbers.append(n)
    tempResult = False
    n += 2
print (numbers[10000])

            