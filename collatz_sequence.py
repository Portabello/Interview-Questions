import sys
sys.setrecursionlimit(10000)

def collatz_sequence(n, sequence = []):
    # if even
    if n % 2 == 0:
        if n/2 == 1:
            #print("converged to 1...")
            return len(sequence)
        else:
            sequence.append(n/2)
            #print("appended..."+str(int(n/2)))
            collatz_sequence(n/2, sequence)
    #if odd
    else:
        if 3*n+1 == 1:
            #print("converged to 1...")
            return len(sequence)
        else:
            sequence.append(3*n+1)
            #print("appended..."+str(int(3*n+1)))
            collatz_sequence(3*n+1, sequence)

n = 234
collatz_sequence(n)

maxLen = None
maxIndex = None
for x in range(0,1000000):
    if collatz_sequence(x) > maxLen:
        maxLen = collatz_sequence(x)
        maxIndex = x
print("max index: "+str(maxIndex)+"    max length: "+str(maxLen))
