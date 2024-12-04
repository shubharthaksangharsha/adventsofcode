def two_d_file_input(filename):
    reports = [] 
    with open(filename, 'r') as f:
         lines = f.readlines()
    for line in lines: 
         levels = list(map(int, line.split()))
         reports.append(levels)
    return reports 

def strictly_increase(level):
    for i in range(1, len(level)):
        if level[i] < level[i - 1]:
            return False 
    return True 

def stricly_decrease(level):
    for i in range(1, len(level)):
        if level[i] > level[i - 1]:
            return False 
    return True 

def check_adj(level):
    for i in range(1, len(level)):
        if abs(level[i] - level[i - 1]) < 1 or abs(level[i] - level[i - 1]) > 3:
            return False 
    return True 

def solve(reports):
    safe_reports = 0
    increase_order, decrease_order = False, False
    for level in reports: 
        if strictly_increase(level):
            increase_order = True 
        elif stricly_decrease(level):
            decrease_order = True 
        if increase_order or decrease_order:
            if check_adj(level):
                safe_reports += 1
        increase_order, decrease_order = False, False
    return safe_reports

if __name__ == '__main__':
    reports = two_d_file_input(filename='inputs/input2.txt')
    print(solve(reports))