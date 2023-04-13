n = input().split("-")
flags = []
if len(n) != 3 or len(n) != 4:
    print("NO")
if len(n) == 4:
    if n[0] != 7:
        print("NO")
    else:
        for num in n:
            flags.append(num.isdigit())
        if len(n[1]) == len(n[2]) == 3 and len(n[3]) == 4 and False not in flags:
            print("YES")
        else:
            print("NO")
if len(n) == 3:
    for num in n:
        flags.append(num.isdigit())
    if len(n[0]) == len(n[1]) == 3 and len(n[2]) == 4 and False not in flags:
        print("YES")
    else:
        print("NO")
