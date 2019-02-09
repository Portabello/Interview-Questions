

def power(num, power):
    return num ** power

def pwr(num, power):
    ans = num
    for x in range(1, power):
        ans = ans * num
    return ans


print(pwr(3, 1))
