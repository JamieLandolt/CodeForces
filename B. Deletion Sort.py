import sys

tests = int(sys.stdin.readline().strip())
for _ in range(tests):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print(1)
            break
    else:
        print(n)
