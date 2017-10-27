def euler_1(threshold, multiples):
    total = 0
    for i in range(0,threshold):
        for x in multiples:
            if i%x == 0:
                total += i
                break
    return total


def euler_2(max_value):
    previous = 1
    current = 2
    result = 2
    while current < max_value:
        new_previous = current
        current = previous + current
        previous = new_previous
        if current%2 == 0 and current < max_value:
            result += current
    return result

print euler_1(threshold=10, multiples=[3,5])
print euler_2(max_value=90)
