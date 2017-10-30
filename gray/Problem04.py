palindromeProduct = 0

val1 = 100
val2 = 100

while val1 < 1000:
    
    while val2 < 1000:
        if str(val1 * val2) == str(val1 * val2)[::-1]:
            if palindromeProduct < (val1 * val2):
                palindromeProduct = (val1 * val2)
        val2 += 1
    val2 = 100
    val1 +=1

print (palindromeProduct)

