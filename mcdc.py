""" calculate number of required test cases for different coverage criteria
1. statement coverage
2. decision coverage
3. condition coverage
4. condition/decision coverage
5. modified condition/decision coverage
6. multiple condition coverage

for a program that has n binary input conditions
"""

def foo(B,C):
    """ example function consists of one if statement A,
    conditions B,C and decision D 
    for this program to work we need a friendly function that is able to return the number of statements and decisions that were called 
    """
    
    if B and C:
        A=True
        D=True
    else:
        A=True
        D=False
    return [A,B,C,D]

from inspect import signature

def tc_sc(foo):
    """ calculates (number of) required test cases for foo
    for condition coverage criterion. for that all possible
    test cases (multiple condition coverage) are run and we
    search for the smallest subset that satisfies condition
    coverage

    >>> tc_sc(foo)
    2
    """

    # get number of input parameters (=conditions)
    sig=signature(foo)
    n=len(sig.parameters)
    
    # generate all possible test cases
    all_test_cases=tc_gen(n)

    # generate all subsets of test cases
    allsubsets=powerset(all_test_cases)

    # create list with all subsets that satisfy cc and their length
    satisfies_cc=[]
    for subset in allsubsets:
        if is_cc(subset):
            satisfies_cc.append((subset,len(subset)))
    satisfies_cc.sort(key=lambda x: x[1])
    return satisfies_cc[0][1]
        

import itertools

def tc_gen(n):
    """ n is the number of conditions

    >>> len(tc_gen(2))
    4
    """
    comb = itertools.product([True,False], repeat=n) 
    return list(comb)

from itertools import chain, combinations

def powerset(iterable):
    """ return all subsets of a sets as tuples
    >>> powerset([[True,False],[False,True]])
    [([True, False],), ([False, True],), ([True, False], [False, True])]
    """
    
    s = list(iterable)
    subsets = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    tuples=list(subsets)
    tuples.remove(())
    return tuples

def is_cc(test_cases):
    """ return true if set of test cases satisfies condition coverage criteria

    >>> is_cc(([True,True],[False,False]))
    True
    >>> is_cc(([True,False],[False,True]))
    True
    >>> is_cc(([False,True],[False,False]))
    False
    >>> is_cc(([True, False],))
    False
    >>> is_cc(([True, False, False], [False, True, True], [True, True, False]))
    True
    >>> is_cc(([True, False, False], [False, True, False], [True, True, False]))
    False
    """
    
    n_inputs=len(test_cases[0])
    cc=[]
    was_true=False
    was_false=False
    
    for input in range(n_inputs):
        was_true=False
        was_false=False
        for test_case in test_cases:
            if test_case[input] == True:
                was_true=True
            else:
                was_false=True
        if was_true and was_false:
            cc.append(True)
        else:
            cc.append(False)      
    return all(cc)


    
