import sys

tests = int(sys.stdin.readline().strip())
for _ in range(tests):
    n = int(sys.stdin.readline().strip())
    string = sys.stdin.readline().strip()
    if all(map(lambda x: x == string[0], string)) or string == "01":
        print("Bob")
        continue
    zero = string.find("1")
    if string[zero + 1:].find("0") != -1:
        print("Alice")
    else:
        print("Bob")
