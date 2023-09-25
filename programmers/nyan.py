import sys
paper = [[0]*100 for i in range(100)]
xy = [0, 0]
for i in range(int(sys.stdin.readline().strip())) :
    xy[0], xy[1] = map(int, sys.stdin.readline().rstrip().split())
    for j in range(xy[0], xy[0]+10) :
        for k in range(xy[1], xy[1]+10) :
            paper[-k][j-1] = 1
sumV = 0
for i in range(100) :
    sumV += sum(paper[i])
print(sumV)