from itertools import permutations
import numpy
from math import factorial


def strategy(n, lst):
    """
    :return:
    """
    skipped = max(lst[:n])
    for j in lst[n:]:
        if j >= skipped:
            return j
    return 0


def golden_rule(N):
    """
    :return:
    """
    probabilities = [0] * (N - 1)
    if N == 1:
        raise IndexError()
    if N >= 7:
        lst_sets = [numpy.random.permutation(N) for x in range(10000)]
    else:
        lst_sets = list(permutations([i for i in range(N)]))
    for n in range(1, N - 1):
        for lst in lst_sets:
            local_max = strategy(n, lst)
            curr_max = max(lst)
            if local_max == curr_max:
                probabilities[n] += 1
    res = list(map(lambda x: x / factorial(N), probabilities))
    a = max(res)
    return res.index(a) / N, lst_sets




def main():
    y = []
    x = []
    for N in range(2, 15):
        permuts = golden_rule(N)[1]

main()