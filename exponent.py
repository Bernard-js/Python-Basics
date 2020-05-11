def exp_while(base, exponent):
    baseOrigin = base
    while(exponent > 1):
        base *= baseOrigin
        exponent -= 1
    return base
    
def exp_for(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result 


print(2 ** 3)
print(exp_while(2, 3))

print(4 ** 5)
print(exp_for(4, 5))