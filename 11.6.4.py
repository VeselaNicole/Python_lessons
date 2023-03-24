n = input()
n = int(n[1:])
program = []
for i in range(n):
    program.append(input())
for line in program:
    if "#" in line:
        hash_index = line.index('#')
        line = line[:hash_index].rstrip()
    print(line)