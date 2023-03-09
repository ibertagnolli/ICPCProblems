r, f = [int(i) for i in input().split(' ')]
print(['up', 'down'][round(f/r)%2])

