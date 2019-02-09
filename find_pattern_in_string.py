

def find_pattern(pattern, str):
    strLen = len(str)
    ans = []
    for x in range(0,strLen-1):
        if pattern == str[x:x+len(pattern)]:
            ans.append(x)
    return ans

pattern = "abr"
str = "abracadabra"
print(find_pattern(pattern, str))
