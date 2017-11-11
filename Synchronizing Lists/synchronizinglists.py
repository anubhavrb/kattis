import sys

def sync(list1, list2):

    sort1 = sorted(list1)
    sort2 = sorted(list2)
    
    sort_dict = {}
    
    for i in range(len(list1)):
        sort_dict[sort1[i]] = sort2[i]
        
    for i in range(len(list1)):
        print sort_dict[list1[i]]
        
    print


f = sys.stdin
n = int(f.readline())

list1 = []
list2 = []

while n != 0:
    for i in range(n):
        list1.append(int(f.readline()))
    
    for i in range(n):
        list2.append(int(f.readline()))
        
    #function that prints out the synchronized second list    
    sync(list1, list2)
    
    n = int(f.readline())
    list1 = []
    list2 = []

