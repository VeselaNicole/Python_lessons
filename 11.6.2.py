list = input().split()
for i in range(len(list)):
    list[i] = int(list[i])
max_num = max(list)
min_num = min(list)
max_index = list.index(max_num)
min_index = list.index(min_num)
list[max_index] = min_num
list[min_index] = max_num
print(*list)