""" 
calculate number of required test cases for different coverage criteria
1. decision coverage
2. condition coverage
3. condition/decision coverage
4. modified condition/decision coverage
5. multiple condition coverage

for a program that has n binary input conditions
"""


def foo(A,B,C):
    """ example function inputs conditions and returns decision D """
    
    if A and (B or C):
        D=True
    else:
        D=False
    return D

from inspect import signature

def tc_cc(foo):
    """ 
    calculates (number of) required test cases for foo
    for condition coverage criterion. for that all possible
    test cases (multiple condition coverage) are run and we
    search for the smallest subset that satisfies condition
    coverage

    >>> tc_cc(foo = lambda A,B,C: A and (B or C))
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
        
def tc_mcdc(foo):
    """ 
    calculates (number of) required test cases for foo
    for modified condition decision coverage criterion. for that all possible
    test cases (multiple condition coverage) are run and we
    search for the smallest subset that satisfies condition
    coverage

    >>> tc_mcdc(foo = lambda A,B: A and B)
    3
    """

    # get number of input parameters (=conditions)
    sig=signature(foo)
    n=len(sig.parameters)
    
    # generate all possible test cases
    all_test_cases=tc_gen(n)

    # generate all subsets of test cases
    allsubsets=powerset(all_test_cases)

    # create list with all subsets that satisfy cc and their length
    satisfies_mcdc=[]
    for subset in allsubsets:
        #print(subset)
        if is_mc(subset,foo) and is_cc(subset) and is_dc(subset,foo):
            satisfies_mcdc.append((subset,len(subset)))
    satisfies_mcdc.sort(key=lambda x: x[1])
    return satisfies_mcdc[0]

import itertools

def tc_gen(n):
    """ n is the number of conditions

    >>> tc_gen(2)
    [[True, True], [True, False], [False, True], [False, False]]
    """
    comb = (list(tuple) for tuple in itertools.product([True,False], repeat=n))
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

def is_dc(test_cases,foo):
    """
    return true if set of test cases satisfies decision coverage criteria
    
    >>> is_dc(([True, False],),foo = lambda A,B: A and B)
    False
    >>> is_dc(([True, False], [True, True]),foo = lambda A,B: A and B)
    True
    """
    
    was_true=False
    was_false=False
    if len(test_cases)==1:
        return False
    else:    
        for test_case in test_cases:
            if foo(*test_case) == True:
                was_true=True
            if foo(*test_case) == False:
                was_false=True
        return was_true and was_false

def is_mc(test_cases, foo):
    """ 
    return true if set of test cases satisfies modified decision condition 
    coverage criteria. each condition needs to independently affect the outcome of the decision

    >>> is_mc(([True,True],[False,True],[True,False]), foo = lambda A,B: A and B)
    True
    >>> is_mc(([False,False],[False,True],[True,False]), foo = lambda A,B: A and B)
    True
    >>> is_mc(([True, True], [False, False]), foo = lambda A,B: A and B)
    False
    >>> is_mc(([True, True, True], [False, False, False]), foo = lambda A,B,C: A and (B or C))
    0
    """
    
    mc=[]
    changed_decision=[]
    for test_case in test_cases:
        mod_test_cases=modify(test_case)
        
        for (mod_test_case,i) in mod_test_cases:
            changed_decision.append((foo(*test_case)!=foo(*mod_test_case),i))
    print(changed_decision)
    
    n=len(test_cases[0])
    did_affect=False
    for condition in range(n):
        did_affect=0
        for i_tc in range(len(changed_decision)):
            #print(i_tc)
            if condition == changed_decision[i_tc][1]:
                did_affect=changed_decision[i_tc][0]
            if did_affect:
                break
        mc.append(did_affect)
    #print(mc)
    return all(mc)

def modify(test_case):
    """ return iterable of modifications and modified index
        [True, False]->[False, False],0
        [True, False]->[True, True],1
        
        we get n modified test cases for n conditions
    
    >>> modify([True, False])
    [([False, False], 0), ([True, True], 1)]
    """
    #test_case=list(test_case)
    #print(test_case)
    n=len(test_case)
    mod_test_cases=[]
    for i in range(n):
        mod_test_case=test_case[:]
        #print(mod_test_case[i])
        mod_test_case[i]= not mod_test_case[i]
        mod_test_cases.append((mod_test_case,i))
    return mod_test_cases

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #print(tc_mcdc(foo))


    
