# -*- coding: utf-8 -*-
'''
Successive approximation is a general method in which on each iteration of an algorithm,
we find a closer estimate of the answer for which we are seeking.
One class of successive approximation algorithms uses the idea of a fixed point.
If f(x) is a mathematical function, then finding the x such that f(x) = x gives us the fixed point of f.
'''
def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess
'''
Assuming you have corrected the implementation of the fixedPoint function,
we can use it to compute other useful things such as square roots.
'''

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)

'''
This code has a bug in it. You can fix this by correcting exactly one
line of the definition. Please do so in the box below.
'''

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)
