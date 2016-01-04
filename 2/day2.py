import sys
import re

s = 0
for line in sys.stdin:
    m = re.search('(\d+)x(\d+)x(\d+)', line)
    l = int(m.group(1))
    h = int(m.group(2))
    w = int(m.group(3))

    if l < h:
        m1 = l
        m2 = h
    else:
        m1 = h
        m2 = l

    if w < m2:
        m2 = m1
        m1 = w

    s = s + 2*l*h + 2*l*w + 2*w*h + m1*m2

print s