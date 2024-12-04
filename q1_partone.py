from typing import List 

def open_file(filename):
    l1, l2 = [], []
    with open(filename, 'r') as f: 
        lines = f.readlines()
    for line in lines: 
        n1, n2  = tuple(map(int, line.split()))
        l1.append(n1)
        l2.append(n2)
    return l1, l2 

def f(l1: List[int], l2: List[int]): 
    # res = [] #ans: 1660292
    #Brute force - O(n^2)
    # while l1 != [] and l2 != []: 
    #     n1, n2 = min(l1), min(l2)
    #     res.append(abs(n1 - n2))
    #     l1.remove(n1)
    #     l2.remove(n2)
    # return sum(res)
    
    #better approach NlogN
    l1, l2, i, j = sorted(l1), sorted(l2), 0, 0 
    res = 0
    for i, j in zip(l1, l2):
        res += abs(i - j)
    return res

if __name__ == '__main__':
    l1, l2 = open_file('inputs/input.txt')
    
    print(f(l1, l2))
    
    
    
    
