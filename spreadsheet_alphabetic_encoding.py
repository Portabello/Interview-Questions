

def find_alphabetic_encoding(n):
    print("n: "+str(n))
    ans = [0, 0, 0]
    ans[2] = n % 26
    ans[1] = int(n / 26) % 26
    ans[0] = int((int(n / 26))/26) % 26
    print(ans)
    output = ""
    for x in ans:
        if x == 0:
            pass
        else:
            output += chr(x+64)
    print("answer: "+output)



find_alphabetic_encoding(27)
