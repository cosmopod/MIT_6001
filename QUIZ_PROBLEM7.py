# -*- coding: utf-8 -*-
'''
McDonald’s sells Chicken McNuggets in packages of 6, 9 or 20 McNuggets. Thus, it is possible,
for example, to buy exactly 15 McNuggets (with one package of 6 and a second package of 9),
but it is not possible to buy exactly 16 McNuggets, since no non- negative integer
combination of 6's, 9's and 20's add up to 16. To determine if it is possible to buy exactly
n McNuggets, one has to find non-negative integer values of a, b, and c such that 6a+9b+20c=n
Write a function, called McNuggets that takes one argument, n, and returns True if it is possible
to buy a combination of 6, 9 and 20 pack units such that the total number of McNuggets equals n,
and otherwise returns False. Hint: use a guess and check approach
'''

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    packages = (6, 9, 20)
    a = packages[0]
    b = packages[1]
    c = packages[2]
    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                if a*x + b*y + c*z == n:
                     return True
    return False

print McNuggets(15)
