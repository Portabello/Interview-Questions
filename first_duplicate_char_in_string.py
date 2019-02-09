
def first_duplicate(str):
    strLen = len(str)
    for x in range(0,strLen):
        for y in range(x-1, 0, -1):
            if str[x] == str[y]:
                return str[x]
str = "abcdddwerwe"
print(first_duplicate(str))
