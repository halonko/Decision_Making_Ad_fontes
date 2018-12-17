from itertools import permutations
import numpy
import math
import matplotlib.pyplot as pyplot


def decision(permutation, n): # [1,2,3,4,7], 2
    mx = max(permutation[:n])
    for j in permutation[n:]:
        if j > mx:
            return j
    return permutation[-1]

def compare(N, number): # length of lst set
    if N == 1:
        raise IndexError()
    if N >= 7:
        lst_sets = [numpy.random.permutation(N) for x in range(1000)]
    else:
        lst_sets = list(permutations([i for i in range(N)]))
    dec_expect = 0
    for i in range(len(lst_sets)):
        dec_expect += decision(lst_sets[i], number)
    return dec_expect/len(lst_sets)


def comparing_interface(Number):
    lst = list()
    for i in range(1, Number):
        lst.append(compare(Number, i))
    return lst


def main():
    Decision = 500
    result = comparing_interface(Decision)
    data, = pyplot.plot(result)
    golden_rule, = pyplot.plot([Decision/math.e, Decision/math.e], [0, Decision],label='Golden rule')
    if result.index(max(result)) == 0:
        maximized_value = 0
    else:
        maximized_value = result.index(max(result))-1
    optimal_decision, = pyplot.plot([maximized_value, maximized_value], [0,Decision], label='Global maximum')
    pyplot.xlabel("Decision values")
    pyplot.ylabel("Expectations given this decision")
    pyplot.legend([data, golden_rule, optimal_decision], ['Observed data', 'Golden rule', 'Global Max'])
    pyplot.show()

main()