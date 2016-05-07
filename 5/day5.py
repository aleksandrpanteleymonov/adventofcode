import sys

i = 0
for line in sys.stdin:
    k = 0
    l = 0
    p = 1
    c1 = ''
    for c in line:
        if c in "aeiou":
            k += 1
        if c == c1:
            l = 1
        if c1 + c in ["ab", "cd", "pq", "xy"]:
            p = 0
        c1 = c
    if k * l * p > 0 and k >= 3:
        i += 1

print i
