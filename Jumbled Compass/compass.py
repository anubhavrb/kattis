import sys

f = sys.stdin

current = int(f.readline())
correct = int(f.readline())

if current < correct:
    cw = correct - current
    acw = 360 - correct + current

else:
    cw = 360 - current + correct
    acw = current - correct

if cw <= acw:
    print cw
else:
    print -1*acw