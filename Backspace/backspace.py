import sys

def main():
    
    f = sys.stdin
    code = f.readline().strip()
    
    result = ""
    i = len(code) - 1
    jump = 0
    while (i >= 0):
        
        if code[i] != "<":
            if jump == 0:
                result = code[i] + result
            else:
                jump -= 1
                
        else:
            jump += 1
        i -= 1
        
    print result
    
if __name__ == "__main__":
    main()