import sys

def main():
    
    f = sys.stdin
    n = int(f.readline().strip())
    
    while n != 0:
        plaintext = f.readline().strip().replace(" ", "").upper()
        encrypt(plaintext, n)
        n = int(f.readline())

def encrypt(plaintext, n):

    length = len(plaintext)
    
    if length <= n:
        print plaintext
    
    else:
        encrypted = range(length)
        index = 0
        offset = 0
        for i in range(length):
            encrypted[index] = plaintext[i]
            index = index + n
            if index >= length:
                offset = offset + 1
                index = offset
                
        print "".join(encrypted)
if __name__ == "__main__":
    main()
    