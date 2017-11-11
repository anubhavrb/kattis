import sys

def main():
    f = sys.stdin
    n = int(f.readline())
    
    records = {}
    
    for i in range(n):
        input = f.readline().split()
        action = input[0]
        name = input[1]
        
        if name not in records.keys():
            records[name] = 0
        
        if action == "entry":
            if records[name] == 1:
                print name, "entered (ANOMALY)"
            else:
                print name, "entered"
                records[name] = 1
            
        else:
            if records[name] == 0:
                print name, "exited (ANOMALY)"
            else:
                print name, "exited"
                records[name] = 0

    
if __name__ == "__main__":
    main()