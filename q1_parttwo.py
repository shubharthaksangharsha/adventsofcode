from q1_partone import open_file 

def find_simlarity_score(l1, l2):
    #brute force O(n^2)
    # res = [] 
    # for i in l1:
    #     count = 0  
    #     for j in l2: 
    #         if i == j: 
    #             count += 1 
    #     res.append(i * count)
    # return sum(res)

    # better approach
    dict = {} 
    for i in l2: 
        if i in dict: 
            dict[i] += 1 
        else:
            dict[i] = 1 
    res = 0
    for i in l1: 
        if i in dict:
           res += i * dict[i]
    return res 

if __name__ == '__main__':
    l1, l2 = open_file('inputs/input.txt')
    print(find_simlarity_score(l1, l2))