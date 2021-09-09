def toRoman(numb:int):
    symbol=["I","IV","V","IX","X","XL","L","XC","C"]
    val=[1,4,5,9,10,40,50,90,100]
    roman=""
    i=8
    while numb!=0:
        if numb>=val[i]:
            roman+=symbol[i]
            numb-=val[i]
        else: i-=1
    return roman

# page=[]
symbol=["I","V","X","L","C"]
nub=[0,0,0,0,0]
N=int(input())
for i in range(1,N+1):
    ans=toRoman(i)
    # page.append(ans)
    for ele in ans:
        for j in range(5):
            if ele==symbol[j]:
                nub[j]+=1
# print(page)
for e in nub:print(e,end=" ")