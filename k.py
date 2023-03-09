num_tasks = int(input())
used = set()
task_list = []
for i in range(num_tasks):
    task_list.append(int(input()))
count = 0
curr_tool = task_list[0]
permutations = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,1,0], [2,0,1]]


