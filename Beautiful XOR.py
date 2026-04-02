import sys

num_tests = int(sys.stdin.readline().strip())
for test in range(num_tests):
    a, b = map(int, sys.stdin.readline().strip().split())

    target = bin(b)[2:]

    current = bin(a)[2:]
    count = 0

    if len(current) != len(target):
        # Pad
        if len(current) > len(target):
            target = "0" * (len(current) - len(target)) + target
        else:
            current = "0" * (len(target) - len(current)) + current
    if current == target:
        print(0)
    else:
        nums = []
        count = 0
        while current != target:
            xor_num = 0
            for i, (bc, bt) in enumerate(zip(current[::-1], target[::-1])):
                if bc != bt:
                    if bc == "0":
                        xor_num += 1 << i
                        if xor_num > int(current, 2):
                            xor_num &= 2 ** i - 1
                            break
                    else:
                        xor_num += int(bc) << i

            nums.append(str(xor_num))
            current = int(current, 2) ^ xor_num
            current = bin(current)[2:]

            if len(current) != len(target):
                # Pad
                if len(current) > len(target):
                    target = "0" * (len(current) - len(target)) + target
                else:
                    current = "0" * (len(target) - len(current)) + current

            count += 1
            if count == 100:
                print(-1)
                break
        else:
            print(count)
            print(' '.join(nums))
