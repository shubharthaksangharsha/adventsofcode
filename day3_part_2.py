"""
--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""
def input(filename): 
    with open(filename, 'r') as f: 
        lines = f.readlines() 
    return lines

def new_instructions(memory): 
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    #TODO 
    pass 

def get_safe_memory(memory):
    sum_result = 0 
    index = 0 
    while index < len(memory): 
        start_index = memory.find('mul(', index)
        if start_index == -1:
            break # no sequence found 
        end_index = memory.find(')', start_index) # found) 
        if end_index == -1:
            break #n no ')' found
        content = memory[start_index + 4: end_index]
        if ',' in content: 
            x, y = content.split(',', 1)
            #validation 
            if x.isdigit() and y.isdigit() and 1 <= len(x) <= 3 and 1 <= len(y) <= 3: 
                print(x, y)
                sum_result += int(x) * int(y)
            else: #can there be another expression between ()
                index = start_index + 1 
                continue 
        index = end_index + 1 
    return sum_result      

def solve(memories): 
    ans = 0
    for memory in memories: 
        ans += get_safe_memory(memory)
    return ans

if __name__ == '__main__':
    memories = input(filename='inputs/input4.txt')
    print(solve(memories))