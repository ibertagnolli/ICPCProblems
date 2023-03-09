import sys
n = int(input())
l = [int(i) for i in sys.stdin.readline().strip().split(' ')]
numout = 0
output = []
while len(l) > 0:
    currmax = l[0]
    curanswer = []
    idx = []
    idx.append(0)
    curanswer.append(l[0])
    for i in range(len(l)):
        if l[i] > currmax:
            currmax = l[i]
            curanswer.append(l[i])
            idx.append(i)
    popcounter = 0
    for i in range(len(idx)):
        l.pop(idx[i]-popcounter)
        popcounter+=1
    output.append(curanswer)
    numout+=1
    print(numout)
    for i in range(numout):
        print(''.join([str(j) for j in output[i]]))
