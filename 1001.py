row,col = [int(x) for x in input().split()]
draw_map= [input() for i in range(row)]
brick=[int(x) for x in input().split()]

ans=""
brickFall=False
for j in range(col):
    for i in range(row):
        if brick[j]!=0:
            if draw_map[0][j]=="O":
                break
            elif i==row-1: brickFall=True  
            elif draw_map[i+1][j]=="O": brickFall=True
            if brickFall==True:
                brickFall=False
                for b in range(brick[j]):
                    if i-b>=0:
                        ans=draw_map[i-b][0:j]+"#"+draw_map[i-b][j+1:]
                        draw_map[i-b]=ans
                break
        else: break
for ele in draw_map:
    print(ele)
                    
            
