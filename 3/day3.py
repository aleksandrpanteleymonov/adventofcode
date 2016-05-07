import sys

s = 0
m = {}
x = 0
y = 0
for line in sys.stdin:
    for c in line:
        m[str(x) + ',' + str(y)] = 1
        if c == '^':
            x -= 1
        if c == 'v':
            x += 1
        if c == '<':
            y -= 1
        if c == '>':
            y += 1

print len(m)
