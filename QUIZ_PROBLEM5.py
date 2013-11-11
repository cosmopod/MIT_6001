# -*- coding: utf-8 -*-
'''
Suppose you are given two strings (they may be empty), s1 and s2.
You would like to "lace" these strings together, by successively alternating elements of each string (starting with the first character of s1).
If one string is longer than the other, then the remaining elements of the longer string should simply be added at the end of the new string.
For example, if we lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.
'''
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    blendStr = []
    tinyStr = min(s1, s2, key=len)
    for num in range(len(tinyStr)):
        blendStr.append(s1[num])
        blendStr.append(s2[num])
    blendStr = ''.join(blendStr)
    if len(s1) != len(s2):
        tinyStr = len(tinyStr)
        blendStr = blendStr + max(s1, s2, key=len)[tinyStr:]
    return blendStr
