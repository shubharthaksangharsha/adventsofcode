"""
--- Part Two ---
Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3
For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three times; the similarity score again increases by 9.
So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
"""
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