import sys

def sync(list1, list2):
    
    list1 = [10, 5, 5, 20]
    list2 = [30, 50, 15, 80]
    
    sort1 = sorted(list1)
    sort2 = sorted(list2)
    
    sort_dict = {}
    
    for i in range(len(list1)):
        sort_dict[i] = sort2[i]
        
    print sort_dict
    for i in range(len(list1)):
        n = list1[i]
        index = sort1.index(n)
        print sort_dict[index]
        
    print


f = open("sample.in")
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

f.close()