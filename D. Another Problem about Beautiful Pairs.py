import sys

tests = int(sys.stdin.readline().strip())
for i in range(tests):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))

    count = 0
    for i, num in enumerate(a):
        pos = 0
        while i + pos + num < n:
            pos += num
            if a[i] * a[i + pos] == abs(pos):
                count += 1
    print(count)


