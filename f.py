import sys 
import math 

s,t,n = [int(i) for i in sys.stdin.readline().strip().split(' ')]
B = sorted([[int(j) for j  in sys.stdin.readline().strip().split(' ')] for i in range(n)], key=lambda x:x[1] )
if B[0][0] >= s:
    B_new = [B[0]]
    for b_i in B[1:]:
        if b_i[0]<=t:
            break
        if b_i[1] < B_new[-1][1]:
            B_new.append(b_i)
    time = 0.0
    a = s
    for i in range(0, len(B_new)-1):
        m, h = B_new[i]
        time += h * (math.log(a,2)-math.log(B_new[i+1][0], 2))
        a = B_new[i+1][0]
    m , h = B_new[-1]
    time += h * (math.log(a, 2) - math.log(t, 2))
    print(f'{time:0.12e}')
else: 
    print(-1)

