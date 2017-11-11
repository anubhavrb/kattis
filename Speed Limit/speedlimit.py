import sys

f = sys.stdin
n = int(f.readline())

hours = 0
distance = 0
while(n != -1):    
    for i in range(n):
        input = f.readline().split(" ")
        speed = int(input[0])
        
        distance = distance + (speed*(int(input[1]) - hours))
        hours = int(input[1])
        
    print distance, "miles"
    distance = 0
    hours = 0
    n = int(f.readline())