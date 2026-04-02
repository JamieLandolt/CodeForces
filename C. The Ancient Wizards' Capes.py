import sys

tests = int(sys.stdin.readline().strip())
for test in range(tests):
    length = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(a, len(a))

    arr = []
    change = False

    for i in range(len(a)):
        if i != len(a) - 1:
            diff = a[i + 1] - a[i]

            if abs(diff) > 1:
                print(0)
                break

        if i == 0:
            arr.append(1)
        if i == len(a) - 1:
            if arr[i] - arr[i - 1] == 0:
                arr.append(1 - arr[i - 1])
            elif arr[i] - arr[i - 1] == 1:
                arr.append(0)
            elif arr[i] - arr[i - 1] == -1:
                arr.append(1)
        elif diff == 1:
            change = True
            arr.append(0)
        elif diff == 0:
            arr.append(1 - arr[-1])
        else:
            change = True
            arr.append(1)
    else:
        if not change:
            print(2)
        elif sum(arr) == a[0]:
            print(1)
        else:
            print(0)
