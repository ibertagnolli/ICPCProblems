#This is from a kattis competition https://open.kattis.com/contests/tcnift/problems/quickestimate

num_estimates = int(input())
for _ in range(num_estimates):
        line = [x for x in input().split(' ')]
        #print(line)
        print(len(line[0]))