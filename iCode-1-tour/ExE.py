k = int(input())
for m in range(12, 0, -1):
    for d in range(31, 0, -1):
        if m == 2 and d > 28:
            continue
        if m in [4, 6, 9, 11] and d > 30:
            continue
        if sum(map(int, f"{d:02d}{m:02d}")) == sum(map(int, str(k))):
            print(f"{d:02d}.{m:02d}.{k}")
            exit()