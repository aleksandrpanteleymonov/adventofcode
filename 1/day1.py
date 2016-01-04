import sys

j=0
for line in sys.stdin:
    for i in range(0, len(line) - 1):
        if line[i] == '(':
             j = j + 1
	else:
             j = j - 1

print j
