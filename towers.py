import sys


for i, line in enumerate(sys.stdin):
    if i == 0:
        t = int(line.strip())
    elif i % 2 == 1:
        n, k = map(int, line.strip().split())
    else:
        towers = list(map(int, line.strip().split()))
        start_tower = towers[k - 1]
        towers.sort()

        water_level = 0

        for t in towers:
            if t <= start_tower:
                continue

            if t - start_tower > start_tower - water_level:
                print("NO")
                break
            water_level += t - start_tower
            start_tower = t
        else:
            print("YES")
