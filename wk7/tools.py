# Example taken from Gries et al. 2013. Practical Programming: An Introduction to Computer Science Using Python 3

def main():
    ls = [1, 2, 3]
    running_sum(ls)
    print('Running sum of [1, 2, 3] is:', ls)

def running_sum(ls):
    '''Modify ls so that it contains the running sums of its original items.
    E.g., running_sum([1, 2, 3]) returns [1, 3, 6].'''
    for i in range(1, len(ls)):
        ls[i] = ls[i - 1] + ls[i]
    return ls

if __name__ == '__main__':
    main()
