"""
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""
from day2_part_1 import two_d_file_input , stricly_decrease, strictly_increase, check_adj
from typing import List 

def damper(safe_count: int, level: List[int]):
    temp = level.copy() 
    for i in range(len(level)):
        temp = level.copy() 
        temp.remove(temp[i])
        if check_safe(temp):
            safe_count += 1 
            break 
        continue 
    return safe_count

def solve(reports):
    safe_reports = 0
    for level in reports: 
        if check_safe(level):
            safe_reports += 1 
            continue
        safe_reports = damper(safe_reports, level)
    return safe_reports 

def check_safe(level):
    if strictly_increase(level) and check_adj(level) or stricly_decrease(level) and check_adj(level): 
        return True 
    return False 

if __name__ == '__main__':
    # reports = two_d_file_input('inputs/input2.txt')
    reports = two_d_file_input('inputs/test.txt')
    print(solve(reports))