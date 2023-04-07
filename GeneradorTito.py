import random

def FullyAuthomaticGenerator(seed):
    """ This method gives you two lists from 1 to n with random numbers on it, the n value, a random p and k, in the order: first list, second list, n, p, k"""
    random.seed(seed)
    n = random.randint(1,15)
    max_amount_of_elements = random.randint(0,n)
    list_a =[]
    for i in range (1, max_amount_of_elements+1):
        x = random.randint(1,n)
        if x not in list_a:
            list_a.append(x)
    list_a.sort()
    max_amount_of_elements = random.randint(0,n)
    list_b =[]
    for i in range (1, max_amount_of_elements+1):
        x = random.randint(1,n)
        if x not in list_b:
            list_b.append(x)
    list_b.sort()
    p = random.randint(1,6)
    k = random.randint(2,6)
    return list_a, list_b, n, p, k

