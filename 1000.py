def isChain(word1,word2):
    nub=0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            nub+=1
            if nub>2:
                return False
    return True

M=int(input())
N=int(input())
chain=[input() for x in range(N)]
for i in range(N):
    if i+1<N:
        if not isChain(chain[i],chain[i+1]):
            print(chain[i])
            break
else:print(chain[-1])