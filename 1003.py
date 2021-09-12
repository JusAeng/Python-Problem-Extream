def isNugget(N):
    nugget_base=[6,9,20]
    nugget_num=[0]
    for i in nugget_base:
        nugget_num=sorted(nugget_num)
        for j in nugget_num:
            new = i+j
            if new > N: break
            if new not in nugget_num:
                nugget_num.append(new)
    nugget_num=sorted(nugget_num)
    return nugget_num

N=int(input())
ans=isNugget(N)
ans.pop(0)
if len(ans)==0:print('no')
else:
    for ele in ans:
        if ele <=N:
            print(ele)
