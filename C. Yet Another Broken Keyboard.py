import collections
import sys

n, k = map(int, sys.stdin.readline().strip().split())
string = sys.stdin.readline().strip()
keyboard = set(sys.stdin.readline().strip().split())
filtered_string = str(filter(lambda x: x in keyboard, string))

dp = [[collections.deque() for _ in range(len(filtered_string))] for _ in range(len(filtered_string))]

for l in range(len(filtered_string) - 1, -1, -1):
    for r in range(len(filtered_string)):
        if l > r:
            continue
        if r - l == 0:
            dp[l][r] = filtered_string[l]
        elif l != 0:
            prev = dp[l - 1][r].copy()
            prev.appendleft(filtered_string[l])
            prev.append(filtered_string[r])
            dp[l][r] = prev
