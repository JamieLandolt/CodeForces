import sys

num_tests = int(sys.stdin.readline().strip())
for _ in range(num_tests):
    a, b = map(int, sys.stdin.readline().strip().split())

    # even b ->
    #     even a -> k = b // 2
    #     odd a -> if b % 4 == 0 choose k = b // 2 else print(-1)
    # odd b ->
    #    even a -> print(-1)
    #    odd a -> k = b

    if b % 2 == 1:
        if a % 2 == 1:
            print(a * b + 1)
        else:
            print(-1)
    elif a % 2 == 0 or b % 4 == 0:
            print(a * b // 2 + 2)
    else:
        print(-1)

