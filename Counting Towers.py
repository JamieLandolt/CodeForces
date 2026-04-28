import sys

def count_towers(n, dp):
    largest = len(dp) - 1
    if n <= largest:
        return sum(dp[n])

    for i in range(largest + 1, n + 1):
        prev = dp[i - 1]
        non_split = prev[0]
        split = prev[1]
        dp.append(((split + 2 * non_split) % (10 ** 9 + 7), (4 * split + non_split) % (10 ** 9 + 7)))
    return sum(dp[n])

t = int(sys.stdin.readline().strip())
for _ in range(t):
    dp = [(0, 0), (1, 1)]
    print(count_towers(int(sys.stdin.readline().strip()), dp) % (10 ** 9 + 7))
