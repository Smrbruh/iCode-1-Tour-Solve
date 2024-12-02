y = int(input())
for x in range(100, 1000):
    if x + int(str(x)[::-1]) == y:
        print(x)
        break
else:
    print(-1)