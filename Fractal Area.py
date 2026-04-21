stdin = """5
0, 0
0.333333, 0
0.5, 0.288675
0.666667, 0
1, 0"""

pts = []
for i, line in enumerate(stdin.split("\n")):
    if i == 0:
        n = int(line.strip())
        continue
    pts.append(list(map(float, line.strip().split(", "))))
print(pts)

# Calculate distance of each polyline section
dist = lambda p1, p2: ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
for i in range(len(pts) - 1):
    pts[i] = dist(pts[i], pts[i + 1])
pts.pop()
print(pts)

A_poly = 0.5 * (1 / 3) * 0.288675
A_F = A_poly / (1 - sum(map(lambda x: x ** 2, pts)))
A_T = 1 / 2 * (3 / 4) ** 0.5 + 3 * A_F
print(A_T)
