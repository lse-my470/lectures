# Example taken from Gries et al. 2013. Practical Programming: An Introduction
# to Computer Science Using Python 3

def main():
    ls = [1, 2, 3]
    running_sum(ls)
    print('Running sum of [1, 2, 3] is:', ls)

def running_sum(ls):
    '''Modify ls so that it contains the running sums of its original items.
    E.g., running_sum([1, 2, 3]) becomes [1, 3, 6].'''
    for i in range(len(ls)):
        ls[i] = ls[i - 1] + ls[i]

# Standard, file called directly.
# i.e. > python tools.py
if __name__ == '__main__':
    # If the file is being run directly
    # The entry point is main().
    # Here, main is calling our running_sum() function.
    main()
    
# WORKFLOW: > python tools
# 1. Automatically sets special var __name__
# 2. Check if file is run directly (if == '__main__')
# 3. If run directly, execute main() function
# 4. main() calls our function running_sum()
# 5. running_sum runs, output from print statment in main()
# DONE.
