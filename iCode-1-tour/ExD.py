n = int(input())
count = 0
for i in range(1, n + 1):
    if (i % 2 == 1 and i >= 3) and (i % 5 == 0 and i >= 15):
        count += 1
print(count)