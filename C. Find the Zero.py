import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

num_tests = int(sys.stdin.readline().strip())
for test in range(num_tests):
    a, b, c, m = map(int, sys.stdin.readline().strip().split())
    a_total = 0
    b_total = 0
    c_total = 0

    ab = lcm(a, b)

    ab_total = m // ab
    bc_total = m // lcm(b, c)
    ac_total = m // lcm(a, c)
    abc_total = m // lcm(ab, c)

    a_total += 2 * abc_total + 3 * (ac_total + ab_total - 2 * abc_total) + 6 * (m // a - (ac_total + ab_total - abc_total))
    b_total += 2 * abc_total + 3 * (bc_total + ab_total - 2 * abc_total) + 6 * (m // b - (bc_total + ab_total - abc_total))
    c_total += 2 * abc_total + 3 * (bc_total + ac_total - 2 * abc_total) + 6 * (m // c - (bc_total + ac_total - abc_total))

    print(int(a_total), int(b_total), int(c_total))
